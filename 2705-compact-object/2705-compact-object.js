/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {

    // Base case
    if (obj === null || typeof obj !== "object") {
        return obj;
    }

    // If array
    if (Array.isArray(obj)) {
        return obj
            .filter(Boolean)
            .map(compactObject);
    }

    // If object
    const result = {};

    for (const key in obj) {
        if (obj[key]) {
            result[key] = compactObject(obj[key]);
        }
    }

    return result;
};