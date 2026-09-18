class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Build the smallest valid interval for each character
        for c in range(26):
            if first[c] == n:
                continue

            l, r = first[c], last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character starts before our interval
                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                i += 1

            if valid:
                intervals.append((l, r))

        # Choose maximum number of non-overlapping intervals
        # Greedy: sort by ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans