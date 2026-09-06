class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = []

        for i in range(len(position)):
            pos_speed.append([position[i],speed[i]])

        sorted_pos_speed = sorted(pos_speed, reverse=True)
        for i in range(len(sorted_pos_speed)):
            time_left = (target - sorted_pos_speed[i][0])/sorted_pos_speed[i][1]
            if not stack:
                stack.append(time_left)
            elif stack[-1] < time_left:
                stack.append(time_left)

        return len(stack)