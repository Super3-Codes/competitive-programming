class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            size = 0
            for j in range(len(boxes)):#1,1,0
                if(boxes[j] == "1"):
                    size = size + abs(j-i)
            result.append(size)
        return result

                 

