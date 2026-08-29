class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        low = 0
        high = len(self.arr)
        while low < high:
            mid = (low + high) // 2
            if self.arr[mid] < num:
                low = mid + 1
            else:
                high = mid
        self.arr.insert(low, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        mid = n // 2
        if n % 2 != 0:
            return float(self.arr[mid])
        return (self.arr[mid - 1] + self.arr[mid]) / 2.0
