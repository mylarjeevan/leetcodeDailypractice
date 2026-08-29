/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {number[][]}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    
    if (this.length !== rowsCount * colsCount) {
        return [];
    }
    
    const result = Array.from(
        { length: rowsCount },
        () => Array(colsCount)
    );
    
    let index = 0;
    
    for (let col = 0; col < colsCount; col++) {
        
        if (col % 2 === 0) {
            // Top to bottom
            for (let row = 0; row < rowsCount; row++) {
                result[row][col] = this[index++];
            }
        } else {
            // Bottom to top
            for (let row = rowsCount - 1; row >= 0; row--) {
                result[row][col] = this[index++];
            }
        }
    }
    
    return result;
};