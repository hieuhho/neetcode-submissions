class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            arrive_time = (target - pos) / spd
            if not stack or arrive_time > stack[-1]:
                stack.append(arrive_time)
        return len(stack)