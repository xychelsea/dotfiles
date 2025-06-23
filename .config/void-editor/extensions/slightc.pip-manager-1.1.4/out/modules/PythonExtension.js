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
exports.PythonExtension = exports.IPythonExtension = void 0;
const vscode = require("vscode");
const ioc_1 = require("../common/ioc");
const interface_1 = require("../interface");
exports.IPythonExtension = ioc_1.createDecorator('pythonExtension');
let PythonExtension = class PythonExtension {
    constructor(_context) {
        this._context = _context;
        this.updatePythonExtension();
    }
    static Create(instantiation, service) {
        const instance = instantiation.createInstance(this);
        if (service) {
            service.set(exports.IPythonExtension, instance);
        }
        return instance;
    }
    updatePythonExtension() {
        this._pythonExtension = vscode.extensions.getExtension('ms-python.python');
    }
    get pythonExtension() {
        if (this._pythonExtension) {
            return this._pythonExtension;
        }
        this.updatePythonExtension();
        return this._pythonExtension;
    }
    getPythonPath() {
        var _a;
        if (!this.pythonExtension) {
            return '';
        }
        const executionDetails = this.pythonExtension.exports.settings.getExecutionDetails();
        return ((_a = executionDetails === null || executionDetails === void 0 ? void 0 : executionDetails.execCommand) === null || _a === void 0 ? void 0 : _a[0]) || '';
    }
    get pythonPath() {
        return this.getPythonPath();
    }
    waitPythonPath() {
        let timer = null;
        return new Promise((resolve, reject) => {
            const tryResolvePythonPath = () => {
                const pythonPath = this.getPythonPath();
                if (pythonPath) {
                    resolve(pythonPath);
                }
            };
            tryResolvePythonPath();
            timer = setInterval(tryResolvePythonPath, 1000);
        }).finally(() => {
            if (timer !== null) {
                clearInterval(timer);
            }
        });
    }
    waitPythonExtensionInited() {
        return __awaiter(this, void 0, void 0, function* () {
            yield this.waitPythonPath();
        });
    }
    onPythonPathChange(callback) {
        var _a;
        const dispose = (_a = this.pythonExtension) === null || _a === void 0 ? void 0 : _a.exports.settings.onDidChangeExecutionDetails(() => {
            const pythonPath = this.getPythonPath();
            return callback(pythonPath);
        });
        if (dispose) {
            this._context.subscriptions.push(dispose);
        }
    }
    ;
};
PythonExtension = __decorate([
    __param(0, interface_1.IExtensionContext),
    __metadata("design:paramtypes", [Object])
], PythonExtension);
exports.PythonExtension = PythonExtension;
//# sourceMappingURL=PythonExtension.js.map