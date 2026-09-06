class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        for n in range(len(nums)):
            prod = 1
            for i in range(len(nums)):
                if n != i:
                    prod *= nums[i]

            res.append(prod)

        return res