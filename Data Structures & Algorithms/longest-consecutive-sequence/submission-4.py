class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        max_sequence = 1

        for n in nums:
            if n - 1 not in numSet:
                length = 1
                c = n + 1
                while c in numSet:
                    c += 1
                    length += 1
                    if length > max_sequence:
                        max_sequence = length
        return max_sequence

        
        