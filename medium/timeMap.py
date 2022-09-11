class TimeMap:

    def __init__(self):
        self.store = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]  

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr = self.store[key]

            if timestamp < arr[0][1]:
                return ""
            elif timestamp >= arr[-1][1]:
                return arr[-1][0]

            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right)//2
                if arr[mid][1] <= timestamp:
                    if arr[mid + 1][1] > timestamp:
                        return arr[mid][0]
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
            return ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)