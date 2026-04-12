class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)]
        fleet = 0

        cars.sort(reverse=True)
        stack = []

        # for key, val in sorted_dic.items():
        #     stack.append(val)

        # for i in range(len(stack)):
        #     ele = stack.pop()
        #     if stack[-1] < ele:
        #         fleet +=1
        for pos, time in cars:
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
