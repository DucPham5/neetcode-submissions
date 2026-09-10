class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key]) -1

        while left < right:
            mid = (1+ left + right) // 2

            if self.store[key][mid][0] <= timestamp:
                left = mid
            elif self.store[key][mid][0] > timestamp:
                right = mid - 1

        if key not in self.store or not self.store[key]:
            return ""
        if self.store[key][left][0] > timestamp:
            return ""
        
        return self.store[key][left][1]

        
