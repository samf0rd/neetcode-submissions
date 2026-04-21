class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        suffix = [0]
        prefixMax = 0
        suffixMax = 0
        res = 0

        for index in range(0, len(height) - 1):
            prefixMax = max(height[index], prefixMax)
            prefix.append(prefixMax)

        for index in range(len(height) - 1, 0, -1):
            suffixMax = max(height[index], suffixMax)
            suffix.append(suffixMax)
        
        suffix.reverse()

        for index, n in enumerate(height):
            water = min(prefix[index], suffix[index]) - height[index]
            if water > 0:
                res += water
        return res