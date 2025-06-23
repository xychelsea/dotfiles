"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.PackageManager = exports.IPackageManager = exports.necessaryPackage = void 0;
const child_process_1 = require("child_process");
const path = require("path");
const os = require("os");
const vscode = require("vscode");
const axios_1 = require("axios");
const xml2js = require("xml2js");
const utils = require("../utils");
const instantiation_1 = require("../common/ioc/common/instantiation");
const common_1 = require("../interface/common");
var Source;
(function (Source) {
    Source["pypi"] = "https://pypi.python.org/simple";
    Source["tsinghua"] = "https://pypi.tuna.tsinghua.edu.cn/simple";
    Source["aliyun"] = "http://mirrors.aliyun.com/pypi/simple";
    Source["douban"] = "http://pypi.douban.com/simple";
})(Source || (Source = {}));
var Category;
(function (Category) {
    Category["python3"] = "Programming Language :: Python :: 3";
    Category["education"] = "Intended Audience :: Education";
    Category["stable"] = "Development Status :: 5 - Production/Stable";
    Category["empty"] = "";
})(Category || (Category = {}));
const defaultCategory = encodeURI(Category.stable);
exports.necessaryPackage = [
    'pip', 'setuptools', 'wheel'
];
exports.IPackageManager = instantiation_1.createDecorator('packageManager');
let PackageManager = class PackageManager {
    constructor(_pythonPath, output, context) {
        this._pythonPath = _pythonPath;
        this.output = output;
        this.context = context;
        this.source = Source.tsinghua;
        // eslint-disable-next-line @typescript-eslint/naming-convention
        this._test_createPackageInfo = this.createPackageInfo;
        this.updatePythonSource();
        this.context.subscriptions.push(vscode.workspace.onDidChangeConfiguration(this.onConfigUpdate.bind(this)));
    }
    static Create(instantiation, service, pythonPath) {
        const instance = instantiation.createInstance(this, pythonPath);
        if (service) {
            service.set(exports.IPackageManager, instance);
        }
        return instance;
    }
    onConfigUpdate(e) {
        const careConfig = ['source', 'sourceCustom'];
        const checkCareConfigChanged = (careConfig, e) => {
            for (let item of careConfig) {
                if (e.affectsConfiguration(`pip-manager.${item}`)) {
                    return true;
                }
            }
            return false;
        };
        if (checkCareConfigChanged(careConfig, e)) {
            this.updatePythonSource();
        }
    }
    updatePythonSource() {
        const { source, sourceCustom } = vscode.workspace.getConfiguration('pip-manager');
        const getSource = (source) => {
            switch (source) {
                case 'pypi': return Source.pypi;
                case 'tsinghua': return Source.tsinghua;
                case 'aliyun': return Source.aliyun;
                case 'douban': return Source.douban;
                default:
                    return '';
            }
        };
        if (sourceCustom) {
            this.source = sourceCustom;
        }
        else {
            this.source = getSource(source);
        }
    }
    updatePythonPath(path) {
        this._pythonPath = path;
    }
    get defaultPath() {
        return path.join(os.homedir(), '.codejiang', 'python', 'bin', 'python3');
    }
    get pythonPath() {
        return this._pythonPath || this.defaultPath;
    }
    execute(command, args, cancelToken) {
        return new Promise((resolve, reject) => {
            let errMsg = '';
            let out = '';
            const p = child_process_1.spawn(command, args);
            this.output.appendLine(`exec ${command} ${args.join(' ')}`);
            if (cancelToken) {
                cancelToken.onCancellationRequested(() => {
                    this.output.appendLine('cancel command');
                    p.kill();
                });
            }
            p.stdout.on('data', (data) => {
                this.output.appendLine(data);
                out = out + data;
            });
            p.stderr.on('data', (data) => {
                if (!(data.indexOf('WARNING') === 0)) {
                    this.output.appendLine(data);
                    errMsg += data;
                }
            });
            p.on('close', (code) => {
                this.output.appendLine('');
                if (!code) {
                    resolve(out);
                }
                else {
                    const err = new Error(errMsg);
                    err.code = code;
                    reject(err);
                }
            });
        });
    }
    pip(args, cancelToken, showErrorMessage = true) {
        const python = this.pythonPath;
        return this.execute(python, ['-m', 'pip']
            .concat(args)
            .concat([]), cancelToken).catch((err) => {
            if (showErrorMessage) {
                vscode.window.showErrorMessage(err.message);
            }
            return Promise.reject(err);
        });
    }
    pipWithSource(iargs, cancelToken, showErrorMessage) {
        const args = [].concat(iargs);
        if (this.source) {
            args.push('-i', this.source);
        }
        return this.pip(args, cancelToken, showErrorMessage);
    }
    createPackageInfo(pack) {
        let out;
        if (typeof pack === 'string') {
            const [name, version] = pack.split('==');
            out = { name, version: version || undefined };
        }
        else {
            out = Object.assign({}, pack);
        }
        if (!out.name) {
            return null;
        }
        out.toString = () => {
            return `${out.name}${out.version ? `==${out.version}` : ''}`;
        };
        return out;
    }
    tryParsePipListJson(packages) {
        try {
            return JSON.parse(packages.replace(/\n/g, ""));
        }
        catch (e) {
            throw new Error(`Get package failed, please run "pip list --format json" or "pip3 list --format json" check pip support json format: ${e}`);
        }
    }
    getPackageList() {
        return __awaiter(this, void 0, void 0, function* () {
            const packages = yield this.pip(['list', '--format', 'json']);
            return this.tryParsePipListJson(packages);
        });
    }
    getPackageUpdate() {
        return __awaiter(this, void 0, void 0, function* () {
            const updates = yield this.pipWithSource(['list', '--outdated', '--format', 'json']);
            return this.tryParsePipListJson(updates);
        });
    }
    mergePackageListWithUpdate(packInfo, updateInfo) {
        const latestVersionMap = {};
        if (updateInfo && updateInfo.length > 0) {
            updateInfo.forEach((info) => {
                latestVersionMap[info.name] = info.latest_version;
            });
            return packInfo.map((info) => {
                const latestVersion = latestVersionMap[info.name];
                if (latestVersion) {
                    return Object.assign(Object.assign({}, info), { latestVersion });
                }
                return info;
            });
        }
        return packInfo;
    }
    getPackageListWithUpdate() {
        return __awaiter(this, void 0, void 0, function* () {
            let packInfo = yield this.getPackageList();
            try {
                const updateInfo = yield this.getPackageUpdate();
                packInfo = this.mergePackageListWithUpdate(packInfo, updateInfo);
            }
            catch (error) {
                // ignore error
            }
            return packInfo;
        });
    }
    installPackage(iargs, cancelToken) {
        return __awaiter(this, void 0, void 0, function* () {
            const args = ['install', '-U'].concat(iargs);
            yield this.pipWithSource(args, cancelToken);
        });
    }
    addPackage(pack, cancelToken) {
        return __awaiter(this, void 0, void 0, function* () {
            const info = this.createPackageInfo(pack);
            if (!info) {
                throw new Error('Invalid Name');
            }
            const name = info.toString();
            yield this.installPackage([name], cancelToken);
        });
    }
    updatePackage(pack, cancelToken) {
        return __awaiter(this, void 0, void 0, function* () {
            const info = this.createPackageInfo(pack);
            if (!info) {
                throw new Error('Invalid Name');
            }
            const name = info.toString();
            yield this.installPackage(['--upgrade', name], cancelToken);
        });
    }
    addPackageFromFile(filePath, cancelToken) {
        return __awaiter(this, void 0, void 0, function* () {
            if (!filePath) {
                throw new Error('Invalid Path');
            }
            yield this.installPackage(['-r', filePath], cancelToken);
        });
    }
    removePackage(pack) {
        return __awaiter(this, void 0, void 0, function* () {
            const info = this.createPackageInfo(pack);
            if (!info) {
                throw new Error('Invalid Name');
            }
            const name = info.name;
            if (exports.necessaryPackage.includes(name)) {
                return;
            }
            yield this.pip(['uninstall', name, '-y']);
        });
    }
    searchFromPyPi(keyword, page = 1, cancelToken) {
        return __awaiter(this, void 0, void 0, function* () {
            const axiosCancelToken = utils.createAxiosCancelToken(cancelToken);
            const resp = yield axios_1.default({
                method: 'GET',
                cancelToken: axiosCancelToken.token,
                url: `https://pypi.org/search/?q=${keyword}&page=${page}${keyword ? '' : `&c=${defaultCategory}`}`,
            });
            const [resultXml] = RegExp('<ul class="unstyled" aria-label="Search results">[\\s\\S]*?</ul>').exec(resp.data) || [];
            if (!resultXml) {
                return Promise.reject({ type: 'no result' });
            }
            const [paginationXml] = RegExp('<div class="button-group button-group--pagination">[\\s\\S]*?</div>').exec(resp.data) || [];
            const result = yield xml2js.parseStringPromise(resultXml, {
                explicitArray: false,
            });
            const list = [];
            result.ul.li.forEach((item) => {
                const data = {
                    name: item.a.h3.span[0]._,
                    version: item.a.h3.span[1]._,
                    updateTime: item.a.h3.span[2].time.$.datetime,
                    describe: item.a.p._,
                };
                list.push({
                    name: data.name,
                    version: data.version,
                    alwaysShow: true,
                    label: data.name,
                    description: `${data.version}`,
                    detail: data.describe
                });
            });
            let totalPages = 1;
            if (paginationXml) {
                const pagination = yield xml2js.parseStringPromise(paginationXml, {
                    explicitArray: false,
                });
                totalPages = Number(pagination.div.a[pagination.div.a.length - 2]._) || 1;
                if (totalPages < page) {
                    totalPages = page;
                }
            }
            return {
                list,
                totalPages,
            };
        });
    }
    getPackageVersionList(pack, cancelToken) {
        return __awaiter(this, void 0, void 0, function* () {
            const info = this.createPackageInfo(pack);
            if (!info) {
                throw new Error('Invalid Name');
            }
            const name = info.name;
            let versionList = [];
            try {
                yield this.pipWithSource(['install', `${name}==`], cancelToken, false);
            }
            catch (err) {
                const { message } = err;
                const [versions] = /(?<=\(from versions: ).+(?=\))/.exec(message) || [];
                versionList = (versions || '').replace(/\s+/g, '').split(',').filter((version) => (version && version !== 'none')).reverse();
            }
            return versionList;
        });
    }
};
PackageManager = __decorate([
    __param(1, common_1.IOutputChannel),
    __param(2, common_1.IExtensionContext),
    __metadata("design:paramtypes", [String, Object, Object])
], PackageManager);
exports.PackageManager = PackageManager;
//# sourceMappingURL=PackageManager.js.map