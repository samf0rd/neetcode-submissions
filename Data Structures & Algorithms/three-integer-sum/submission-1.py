class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for index, a in enumerate(nums):
            if index > 0 and a == nums[index - 1]:
                continue

            if a > 0:
                break

            left = index + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > -a:
                    right -= 1
                elif nums[left] + nums[right] < -a:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res

