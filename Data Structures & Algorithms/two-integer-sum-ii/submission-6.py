class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        seen = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in seen:
                return [seen[diff] + 1, i + 1]
            seen[n] = i
        return []