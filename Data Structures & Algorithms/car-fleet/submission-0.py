class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_hash = [[p, s] for p, s in zip(position, speed)]
        res = []
        for p, s in sorted(car_hash)[::-1]:
            arr_time = (target - p) / s
            if not res:
                res.append(arr_time)
            elif res[-1] < arr_time:
                res.append(arr_time)
        return len(res)