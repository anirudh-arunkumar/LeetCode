class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)
        running_product = 1

        for i in range(len(nums)):
            output[i] = running_product
            running_product *= nums[i]

        post_product = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post_product
            post_product *= nums[i]
        
        return output
