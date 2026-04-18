class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        max_sequence = 1

        for n in nums:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                    max_sequence = max(length, max_sequence)
        return max_sequence

        
        