class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        def toSeconds(time):
            current=0
            parts=[]
            for ch in time:
                if ch==":":
                    parts.append(current)
                    current=0
                else:
                    current = current * 10 + (ord(ch) - ord('0'))
            parts.append(current)
            return parts[0] * 3600 + parts[1] * 60 + parts[2]

        return toSeconds(endTime) - toSeconds(startTime)
                