class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        
        points1 = []
        points2 = []
        
        # Store coordinates of all 1s
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))
                if img2[i][j] == 1:
                    points2.append((i, j))
        
        count = {}
        ans = 0
        
        # Compare every 1 in img1 with every 1 in img2
        for x1, y1 in points1:
            for x2, y2 in points2:
                shift = (x2 - x1, y2 - y1)
                
                count[shift] = count.get(shift, 0) + 1
                ans = max(ans, count[shift])
        
        return ans