 def similarPairs(self, words):
        count = 0
        for i in range(len(words)):# 
            for j in range(i):#0-4 3 
                if set(words[i]) == set(words[j]):
                    count +=1
        return count
