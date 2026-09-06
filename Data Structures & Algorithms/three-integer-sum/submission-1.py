class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        output = []
        for i in range(len(nums)):
            if i > 0 and sortednums[i] == sortednums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if sortednums[i] + sortednums[left] + sortednums[right] == 0:
                    output.append([sortednums[i],sortednums[left],sortednums[right]])
                    left+=1
                    right-=1
                    while left < right and sortednums[left] == sortednums[left-1]:
                        left+=1
                    while right > left and sortednums[right] == sortednums[right+1]:
                        right-=1
                elif sortednums[i] + sortednums[left] + sortednums[right] > 0:
                    right-=1
                elif sortednums[i] + sortednums[left] + sortednums[right] < 0:
                    left+=1
            
        return output

                
        