class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        def calculation(data):

            months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month=int(data[:2])
            day=int(data[3:])
            total=day
            for i in range(month-1):
                total+=months[i]
            return total
        A_arrive=calculation(arriveAlice)
        B_arrive=calculation(arriveBob)
        A_leave=calculation(leaveAlice)
        B_leave=calculation(leaveBob)
        val1=max(A_arrive,B_arrive)
        val2=min(A_leave,B_leave)
        if val1>val2:
            return 0
        else:
            return val2-val1+1
        
        