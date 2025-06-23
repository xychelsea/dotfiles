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
exports.PackageDataProvider = exports.PackageDataItem = void 0;
const ioc_1 = require("../common/ioc");
const vscode = require("vscode");
const PackageManager_1 = require("./PackageManager");
class PackageDataItem extends vscode.TreeItem {
    constructor(info, collapsibleState) {
        super(info.name, collapsibleState);
        this.info = info;
        this.collapsibleState = collapsibleState;
        const canUpdate = (info.latestVersion && info.latestVersion !== info.version);
        this.name = info.name;
        this.version = info.version;
        this.description = canUpdate ? `${info.version} > ${info.latestVersion}` : info.version;
        this.iconPath = new vscode.ThemeIcon('circle-outline');
        this.tooltip = `${this.name}@${this.description}`;
        this.contextValue = canUpdate ? 'canUpdate' : '';
    }
}
exports.PackageDataItem = PackageDataItem;
;
const IPackageDataProvider = ioc_1.createDecorator('packageDataProvider');
let PackageDataProvider = class PackageDataProvider {
    constructor(pip) {
        this.pip = pip;
        this.isFristUpdate = true;
        this.packageList = [];
        this.packageUpdateList = [];
        this._onDidChangeTreeData = new vscode.EventEmitter();
        this.onDidChangeTreeData = this._onDidChangeTreeData.event;
    }
    static Create(instantiation, service) {
        const instance = instantiation.createInstance(this);
        if (service) {
            service.set(IPackageDataProvider, instance);
        }
        return instance;
    }
    getTreeItem(element) {
        return element;
    }
    requireNextUpdate() {
        this.isFristUpdate = false;
        if (this.nextUpdateTimer) {
            clearTimeout(this.nextUpdateTimer);
        }
        this.nextUpdateTimer = setTimeout(() => {
            this._onDidChangeTreeData.fire();
        }, 100);
    }
    getChildren(element) {
        return __awaiter(this, void 0, void 0, function* () {
            if (element) {
                return Promise.resolve([]);
            }
            else {
                if (this.isFristUpdate) {
                    this.packageList = yield this.pip.getPackageList();
                    /** async fetch update info */
                    this.pip.getPackageUpdate().then((updateInfo) => {
                        this.packageUpdateList = updateInfo;
                    }).finally(() => {
                        this.requireNextUpdate();
                    });
                }
                else {
                    this.isFristUpdate = true;
                }
                const packList = this.pip.mergePackageListWithUpdate(this.packageList, this.packageUpdateList);
                const datalist = packList.map((info) => {
                    return new PackageDataItem(info);
                });
                return Promise.resolve(datalist);
            }
        });
    }
    refresh() {
        this.isFristUpdate = true;
        this._onDidChangeTreeData.fire();
    }
};
PackageDataProvider = __decorate([
    __param(0, PackageManager_1.IPackageManager),
    __metadata("design:paramtypes", [Object])
], PackageDataProvider);
exports.PackageDataProvider = PackageDataProvider;
//# sourceMappingURL=PackageDataProvider.js.map