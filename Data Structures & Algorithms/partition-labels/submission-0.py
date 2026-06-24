class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_seen = {}
        for i, v in enumerate(s):
            last_seen[v] = i

        size = end = 0
        for i, v in enumerate(s):
            size += 1
            end = max(end, last_seen[v])
            if end == i:
                res.append(size)
                size = 0
        return res