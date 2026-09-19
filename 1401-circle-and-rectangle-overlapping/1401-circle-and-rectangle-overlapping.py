class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        # Closest x-coordinate on rectangle to circle center
        x = max(x1, min(xCenter, x2))

        # Closest y-coordinate on rectangle to circle center
        y = max(y1, min(yCenter, y2))

        # Squared distance
        dx = xCenter - x
        dy = yCenter - y

        return dx * dx + dy * dy <= radius * radius