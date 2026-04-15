class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #counter but this time we have multiple words
        output = {}

        for word in strs:
            signature = "".join(sorted(word))
            if signature not in output:
                output[signature] = [word]
            else:
                output[signature].append(word)
        return list(output.values())

            