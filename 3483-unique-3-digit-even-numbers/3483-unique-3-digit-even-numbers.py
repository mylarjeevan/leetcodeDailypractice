class Solution(object):
    def totalNumbers(self, digits):
        count = 0

        for a in range(1, 10):      
            for b in range(10):      
                for c in range(0, 10, 2):  

                  
                    temp = [a, b, c]
                    available = digits[:]

                    possible = True

                    for d in temp:
                        if d in available:
                            available.remove(d)
                        else:
                            possible = False
                            break

                    if possible:
                        count += 1

        return count