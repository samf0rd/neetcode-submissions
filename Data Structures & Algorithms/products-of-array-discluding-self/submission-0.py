class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        postfix = 1

        for n in nums:
            res.append(prefix)
            prefix = n * prefix
        # In Python, the range(start, stop, step) function has one absolute rule: 
        # It stops BEFORE it hits the stop number.
        for n in range(len(nums) - 1, -1, -1): 
            res[n] = res[n] * postfix
            postfix = nums[n] * postfix
        
        return res