class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, []).append([timestamp, value])
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''

        pairs = self.data[key]
        res = ''
        left, right = 0, len(pairs)-1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res 