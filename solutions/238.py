class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, result = 1, 1, []
        for i in range(len(nums)):
            result.append(left)
            left *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
