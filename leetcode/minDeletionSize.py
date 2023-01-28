def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 0:
            return 0
        lengthOfWords = len(strs[0])
        counter = 0
        for i in range(lengthOfWords):
            min = 0
            for word in strs:
                if(min == 0):
                    min = ord(word[i])
                else:
                    value = ord(word[i])
                    if(min > value):
                        counter += 1
                        break
                    else:
                        min = value
        return counter
