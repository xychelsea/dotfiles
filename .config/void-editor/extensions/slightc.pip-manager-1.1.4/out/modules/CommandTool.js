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
Object.defineProperty(exports, "__esModule", { value: true });
exports.CommandTool = exports.ICommandTool = void 0;
const vscode = require("vscode");
const ioc_1 = require("../common/ioc");
const common_1 = require("../interface/common");
exports.ICommandTool = ioc_1.createDecorator('commandTool');
let CommandTool = class CommandTool {
    constructor(_context) {
        this._context = _context;
        this.emptyCommandMap = new Map();
    }
    static Create(instantiation, service) {
        const instance = instantiation.createInstance(this);
        if (service) {
            service.set(exports.ICommandTool, instance);
        }
        return instance;
    }
    registerEmptyCommand(name) {
        if (Array.isArray(name)) {
            this.registerEmptyCommands(name);
        }
        else {
            this.emptyCommandMap.set(name, vscode.commands.registerCommand(name, () => { }));
        }
    }
    registerEmptyCommands(names) {
        names.forEach((name) => {
            this.registerEmptyCommand(name);
        });
    }
    disposeEmptyCommand(name) {
        const command = this.emptyCommandMap.get(name);
        if (command) {
            command.dispose();
        }
    }
    registerCommand(name, callback, thisArg) {
        this.disposeEmptyCommand(name);
        this._context.subscriptions.push(vscode.commands.registerCommand(name, callback, thisArg));
    }
};
CommandTool = __decorate([
    __param(0, common_1.IExtensionContext),
    __metadata("design:paramtypes", [Object])
], CommandTool);
exports.CommandTool = CommandTool;
//# sourceMappingURL=CommandTool.js.map