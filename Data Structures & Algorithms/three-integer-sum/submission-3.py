class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sortednums = sorted(nums)
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            if sortednums[i] == sortednums[i-1] and i > 0:
                continue
            while left < right:
                if sortednums[i] + sortednums[left] + sortednums[right] == 0:
                    output.append([sortednums[i],sortednums[left],sortednums[right]])
                    left+=1
                    right-=1
                    while sortednums[left] == sortednums[left-1] and left < right:
                        left+=1
                elif sortednums[i] + sortednums[left] + sortednums[right] < 0:
                    left+=1
                elif sortednums[i] + sortednums[left] + sortednums[right] > 0:
                    right-=1
        
        return output

        