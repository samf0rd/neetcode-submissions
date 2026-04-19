class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = defaultdict(list)

        for char in magazine:
            frequency[char] = 1 + frequency.get(char, 0)


        for char in ransomNote:
            if frequency.get(char, 0) > 0:
                frequency[char] = frequency.get(char, 0) - 1
            else:
                return False
        return True

