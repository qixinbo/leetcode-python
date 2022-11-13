class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ##### v1 #####
        # for i in range(len(nums)):
        #     left = sum(nums[:i])
        #     right = sum(nums[i+1:])
        #     # print(left, right)
        #     if left == right:
        #         return i
        # return -1
        sm = sum(nums)
        cur = 0
        for i in range(len(nums)):
            if cur == sm - cur - nums[i]:
                return i
            cur += nums[i]
        return -1
