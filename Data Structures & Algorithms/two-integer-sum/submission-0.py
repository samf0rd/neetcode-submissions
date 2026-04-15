class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, a in enumerate(nums):
            b = target - a
            if b in seen:
                return [seen[b], index]
            else:
                seen[a] = index
    
