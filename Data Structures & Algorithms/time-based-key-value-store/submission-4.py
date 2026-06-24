class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_map.get(key):
            return ""
        l, r = 0, len(self.hash_map[key]) - 1
        recent = ""
        while l <= r:
            m = l + (r - l) // 2
            ts, val = self.hash_map[key][m]
            if ts == timestamp:
                return val
            if ts > timestamp:
                r = m - 1
            else:
                recent = val
                l = m + 1
        return recent
