class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        tracker = [0] * (len(s)+1)
        #tracker = [-1,0,1,0]
        for i in range(len(shifts)):
            start = shifts[i][0]
            end = shifts[i][1]
            direction = shifts[i][2]
            if direction == 0:
               tracker[start] -= 1
               tracker[end+1] += 1
            else:
                tracker[start] += 1
                tracker[end+1] -= 1
        print(tracker)
        prefixSum = 0
        for i in range(len(s)):
            prefixSum += tracker[i]

            newValue = (((ord(s[i]) + prefixSum)-97)%26) + 97
            s = s[:i] + chr(newValue) + s[i+1:]
        return s
