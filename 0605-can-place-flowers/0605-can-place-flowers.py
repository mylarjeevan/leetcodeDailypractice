class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        size=len(flowerbed)
        i=1
        if n>0 and size>0 and flowerbed[0]==0:
            if size==1 or flowerbed[1]==0:
                flowerbed[0]=1
                n-=1
        while i<size-1 and n>0:
            if flowerbed[i-1]!=1 and flowerbed[i+1]!=1 and flowerbed[i]==0:
                flowerbed[i]=1
                n-=1
                i+=2
            else:
                i+=1
        if n>0 and size>1:
            if flowerbed[size-2]==0 and flowerbed[size-1]==0:
                flowerbed[size-1]=1
                n-=1
        return n<1

        