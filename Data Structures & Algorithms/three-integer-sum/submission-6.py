class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        output = []
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            left = i+1
            right = len(sortedNums)-1
            while left < right:
                if sortedNums[i] + sortedNums[left] + sortedNums[right] == 0:
                    output.append([sortedNums[i],sortedNums[left],sortedNums[right]])
                    left+=1
                    right-=1
                    while sortedNums[left] == sortedNums[left-1] and left < right:
                        left+=1
                    
                elif sortedNums[i] + sortedNums[left] + sortedNums[right] > 0:
                    right-=1
                else:
                    left+=1
        return output
        