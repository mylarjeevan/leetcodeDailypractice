class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        A = sum(aliceSizes)
        B = sum(bobSizes)

        diff = (B - A) // 2

        bobSet = set(bobSizes)

        for x in aliceSizes:
            y = x + diff

            if y in bobSet:
                return [x, y]