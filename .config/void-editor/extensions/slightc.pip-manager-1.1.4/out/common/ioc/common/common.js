"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.IdleValue = exports.runWhenIdle = exports.illegalState = void 0;
function illegalState(name) {
    if (name) {
        return new Error(`Illegal state: ${name}`);
    }
    else {
        return new Error('Illegal state');
    }
}
exports.illegalState = illegalState;
class IdleValue {
    constructor(executor) {
        this._didRun = false;
        this._executor = () => {
            try {
                this._value = executor();
            }
            catch (err) {
                this._error = err;
            }
            finally {
                this._didRun = true;
            }
        };
        this._handle = exports.runWhenIdle(() => this._executor());
    }
    dispose() {
        this._handle.dispose();
    }
    get value() {
        if (!this._didRun) {
            this._handle.dispose();
            this._executor();
        }
        if (this._error) {
            throw this._error;
        }
        return this._value;
    }
}
exports.IdleValue = IdleValue;
//# sourceMappingURL=common.js.map