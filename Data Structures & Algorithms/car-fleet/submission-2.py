class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_n_speed = []

        for i in range(len(position)):
            pos_n_speed.append([position[i], speed[i]])

        sort_pos_n_speed = sorted(pos_n_speed, reverse = True)

        for i in range(len(sort_pos_n_speed)):
            time_left = (target-sort_pos_n_speed[i][0]) /sort_pos_n_speed[i][1]
            if not stack:
                stack.append(time_left)
            elif stack[-1] < time_left:
                stack.append(time_left)


        return len(stack) 

        
        