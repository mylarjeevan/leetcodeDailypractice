/**
 * @param {MultiDimensionalArray} arr
 * @param {number} n
 * @return {MultiDimensionalArray}
 */
var flat = function (arr, n) {
    let result = [];

    function flatten(array, depth) {
        for (let item of array) {
            if (Array.isArray(item) && depth > 0) {
                flatten(item, depth - 1);
            } else {
                result.push(item);
            }
        }
    }

    flatten(arr, n);
    return result;
};