"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.createAxiosCancelToken = void 0;
const axios_1 = require("axios");
function createAxiosCancelToken(cancelToken) {
    const axiosCancelToken = axios_1.default.CancelToken.source();
    cancelToken === null || cancelToken === void 0 ? void 0 : cancelToken.onCancellationRequested(() => {
        axiosCancelToken.cancel();
    });
    return axiosCancelToken;
}
exports.createAxiosCancelToken = createAxiosCancelToken;
//# sourceMappingURL=index.js.map