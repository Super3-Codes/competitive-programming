   def compress(self, chars: List[str]) -> int:
        index = 0
        left = 0
        count = 0
        for i in range(len(chars)):
            if chars[i] == chars[left]:
                count += 1
            else:
                chars[index] = chars[left]
                index += 1
                if count > 1:
                    finalCount = str(count)
                    for c in finalCount:
                        chars[index] = c
                        index += 1
                left = i
                count = 1
        chars[index] = chars[left]
        index += 1
        if count > 1:
            finalCount = str(count)
            for c in finalCount:
                chars[index] = c
                index += 1
        return index
