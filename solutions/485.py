class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count = 0
        # max_count = 0
        # for i in range(len(nums)):
        #     if 0 == nums[i]:
        #         count = 0
        #     else:
        #         count += 1
        #         max_count = count if max_count < count else max_count

        # return max_count
        
        count = [0, 0]
        for num in nums:
            if 1 == num:
                count[1] += 1
            else:
                count[1] = 0
            count[0] = max(count[0], count[1])
        return count[0]
