class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        assigned_t_chars = set() # O(1) instant lookup for claimed letters!

        # Zip walks through both strings at the exact same time
        for char_s, char_t in zip(s, t):
            
            # If we haven't seen the 's' letter yet...
            if char_s not in mapping:
                # Check if the 't' letter is already claimed by someone else
                if char_t in assigned_t_chars:
                    return False
                
                # If it's free, create the map and claim the 't' letter
                mapping[char_s] = char_t
                assigned_t_chars.add(char_t)
                
            # If we HAVE seen the 's' letter, make sure it matches its old mapping!
            else:
                if mapping[char_s] != char_t:
                    return False
                    
        return True
    