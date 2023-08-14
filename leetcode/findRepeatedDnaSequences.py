class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        map = {}
        result = set()

        for i in range(len(s) - 9):
            if s[i:i+10] in map:
                result.add(s[i:i+10])
            else:
                map[s[i:i+10]] = 1
        
        return result
