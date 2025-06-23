"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.i18n = exports.I18n = void 0;
const zh_cn_1 = require("./zh-cn");
class I18n {
    constructor() {
        this.locale = 'en';
        this.messages = {};
        this.currentMessage = {};
        if (process.env.VSCODE_NLS_CONFIG) {
            try {
                const config = JSON.parse(process.env.VSCODE_NLS_CONFIG);
                this.locale = config['locale'];
            }
            catch (error) { /* ignore */ }
        }
        this.messages = Object.assign(zh_cn_1.default);
        this.updateLocale(this.locale);
    }
    updateLocale(locale) {
        if (locale) {
            this.locale = locale;
        }
        this.currentMessage = this.messages[this.locale] || {};
    }
    localize(key, defaultValue, ...args) {
        var _a;
        const message = (key && ((_a = this.currentMessage) === null || _a === void 0 ? void 0 : _a[key])) || defaultValue;
        return message.replace(/\%\d+\%/g, (match) => {
            const index = match.replace(/[\%]/g, '');
            return args[Number(index)] || '';
        });
    }
}
exports.I18n = I18n;
exports.i18n = new I18n();
//# sourceMappingURL=localize.js.map