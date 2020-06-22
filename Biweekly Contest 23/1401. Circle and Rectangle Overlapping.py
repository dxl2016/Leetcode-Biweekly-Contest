class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        return (x_center - min(max(x1, x_center), x2)) ** 2 + (y_center - min(max(y1, y_center), y2)) ** 2 <= radius ** 2

