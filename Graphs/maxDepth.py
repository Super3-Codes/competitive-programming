class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxDepthResult = 0

        def dfs(node, depth):
            nonlocal maxDepthResult
            if node is None:
                return
            depth += 1
            maxDepthResult = max(depth, maxDepthResult)
            for child in node.children:
                dfs(child, depth)

        dfs(root, 0)
        return maxDepthResult
