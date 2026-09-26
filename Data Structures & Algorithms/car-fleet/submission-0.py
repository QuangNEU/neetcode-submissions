class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        current_lead_time = 0
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars:
            time = (target-pos)/spd
            if time > current_lead_time:
                res+=1
                current_lead_time = time
        return res