/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const root = new Map();
    const RESULT = Symbol("result");

    return function (...args) {
        let node = root;

        // Traverse the cache using each argument
        for (const arg of args) {
            if (!node.has(arg)) {
                node.set(arg, new Map());
            }
            node = node.get(arg);
        }

        // Return cached result if present
        if (node.has(RESULT)) {
            return node.get(RESULT);
        }

        // Otherwise calculate and cache it
        const result = fn(...args);
        node.set(RESULT, result);

        return result;
    };
}