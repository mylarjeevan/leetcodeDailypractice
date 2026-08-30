class TimeLimitedCache {
    constructor() {
        this.cache = new Map();
    }

    set(key, value, duration) {
        const exists = this.cache.has(key);

        // Remove the previous timer if the key already exists
        if (exists) {
            clearTimeout(this.cache.get(key).timer);
        }

        const timer = setTimeout(() => {
            this.cache.delete(key);
        }, duration);

        this.cache.set(key, { value, timer });

        return exists;
    }

    get(key) {
        if (!this.cache.has(key)) {
            return -1;
        }

        return this.cache.get(key).value;
    }

    count() {
        return this.cache.size;
    }
}