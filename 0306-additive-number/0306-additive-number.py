class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]

                if len(a) > 1 and a[0] == '0':
                    continue
                if len(b) > 1 and b[0] == '0':
                    continue

                k = j

                while k < n:
                    c = str(int(a) + int(b))

                    if not num.startswith(c, k):
                        break

                    k += len(c)
                    a, b = b, c

                if k == n:
                    return True

        return False