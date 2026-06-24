class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        for num, count in seen.items():
            freq[count].append(num)
        
        ans = []
        for i in reversed(freq):
            for num in i:
                ans.append(num)
                if len(ans) == k:
                    return ans