class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # If the set is smaller than the list, a duplicate was removed.
        return len(set(nums)) != len(nums)