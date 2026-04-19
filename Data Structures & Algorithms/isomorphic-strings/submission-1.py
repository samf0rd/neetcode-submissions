class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping = defaultdict(list)
        t = list(t)

        for index, char in enumerate(s):
            if char not in mapping:
                if t[index] in mapping.values():
                    return False
                mapping[char] = t[index]
            else:
                if mapping[char] != t[index]:
                    return False
        return True
    