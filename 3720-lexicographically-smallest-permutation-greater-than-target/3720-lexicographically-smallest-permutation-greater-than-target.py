from collections import Counter

class Solution(object):

    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        count = Counter(s)
        path = []

        # Match target as much as possible
        i = 0

        while i < len(s) and count[target[i]] > 0:
            path.append(target[i])
            count[target[i]] -= 1
            i += 1

        # Backtrack
        while i >= 0:

            # Undo matched character
            if i < len(path):
                ch = path.pop()
                count[ch] += 1

            # Find smallest character greater than target[i]
            if i < len(target):
                for c in sorted(count):
                    if count[c] > 0 and c > target[i]:

                        count[c] -= 1

                        # Remaining characters in sorted order
                        remaining = ""

                        for ch in sorted(count):
                            remaining += ch * count[ch]

                        return "".join(path) + c + remaining

            i -= 1

        return ""