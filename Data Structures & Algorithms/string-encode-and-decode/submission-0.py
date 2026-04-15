class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # Example: 2#hi5#co#de
        while i < len(s):
            # 1. Find the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
                
            # 2. Extract the length and convert it to an integer
            # s[i:j] slices the string from index i up to (but not including) j
            length = int(s[i:j])
            
            # 3. Extract the word! 
            # It starts at j + 1, and goes for 'length' characters.
            word = s[j + 1:j+ length + 1]
            
            # 4. Add it to our list
            res.append(word)
            
            # 5. Move the 'i' pointer to the start of the next encoded chunk
            i = j + length + 1
            
        return res