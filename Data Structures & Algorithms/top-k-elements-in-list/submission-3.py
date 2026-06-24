class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        bucket = [[] for i in range(len(nums) + 1)]
        print('bucket', bucket)
        print('freqs', freqs)
        for num, freq in freqs.items():
            bucket[freq].append(num)
        
        ans = []
        for i in reversed(bucket):
            for num in i:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
            