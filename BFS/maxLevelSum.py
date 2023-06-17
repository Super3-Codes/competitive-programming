# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque ()
        queue.append(root)
        level = 0
        resultSum = inf * -1
        levelCounter = 0
        while queue:
            currentSum = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                currentSum += node.val
                if node.right is not None:
                    queue.append(node.right)
                if node.left is not None:
                    queue.append(node.left)
            levelCounter += 1
            if currentSum > resultSum:
                resultSum = currentSum
                level = levelCounter
        return level 
