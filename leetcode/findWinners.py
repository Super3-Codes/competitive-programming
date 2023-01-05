 def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        losser = defaultdict(int)
        resultOne = []
        resultTwo = []

        for w,l in matches:
            winner[w] +=1
            losser[l] +=1
        for key,value in winner.items():
            if key not in losser:
                resultOne.append(key)
        
        for key,value in losser.items():
           if value == 1:
               resultTwo.append(key)
        return [sorted(resultOne),sorted(resultTwo)]
