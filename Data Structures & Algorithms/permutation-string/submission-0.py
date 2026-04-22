from collections import Counter
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target_dict = Counter(s1) 
        window_dict = defaultdict(int)
        l = 0

        for c in range(len(s1)):
            window_dict[s2[c]] += 1
        
        if target_dict == window_dict:
            return True

        for i in range(len(s1), len(s2)):
            window_dict[s2[i]] += 1
            if window_dict[s2[l]] == 1:
                del window_dict[s2[l]]
            else:
                window_dict[s2[l]] -= 1
            l += 1 
            if target_dict == window_dict:
                return True
        return False