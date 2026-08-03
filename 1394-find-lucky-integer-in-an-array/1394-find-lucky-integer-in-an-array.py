class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash_map = {}

        for num in arr:
            hash_map[num] = hash_map.get(num, 0) + 1

        ans = -1

        for num, freq in hash_map.items():
            if num == freq:
                ans = max(ans, num)

        return ans