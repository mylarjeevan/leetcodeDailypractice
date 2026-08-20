class Solution(object):

    def isHappy(self, n):

        seen = set()

        def find(val):

            if val == 1:
                return True

            elif val in seen:
                return False

            seen.add(val)

            sums = 0
            while val > 0:
                sums += (val % 10) ** 2
                val = val // 10

            val = sums
            return find(val)

        return find(n)