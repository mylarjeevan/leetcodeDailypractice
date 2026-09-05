var cancellable = function(generator) {
    let cancel;

    const cancelPromise = new Promise((_, reject) => {
        cancel = () => reject("Cancelled");
    });

    const promise = (async () => {
        let result = generator.next();

        while (!result.done) {
            try {
                // Wait for either:
                // 1. Current promise to finish
                // 2. cancel() to be called
                const value = await Promise.race([
                    result.value,
                    cancelPromise
                ]);

                // Send resolved value back into generator
                result = generator.next(value);

            } catch (error) {
                // Send error back into generator
                result = generator.throw(error);
            }
        }

        return result.value;
    })();

    return [cancel, promise];
};