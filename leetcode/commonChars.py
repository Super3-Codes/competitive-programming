class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total = {}
        result = []
        for word in words:
            count = {}
            for i in range(len(word)):
                if(word[i] not in count):
                    count[word[i]] = 0
                count[word[i]] += 1
            for key in string.ascii_lowercase:
                if(key not in total):
                    total[key] = inf
                if(key not in count):
                    count[key] = 0
                total[key] = min(total[key] , count[key])

        for key , value in total.items():
            while(value > 0):
                result.append(key)
                total[key] = total[key] - 1
                value = value - 1
        return result
