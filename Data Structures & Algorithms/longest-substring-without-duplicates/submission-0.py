class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        longest = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] not in uniques:
                uniques.add(s[r])
                longest = max(longest, len(uniques))
                r += 1
            else:
                uniques.discard(s[l])
                l += 1
        return longest


