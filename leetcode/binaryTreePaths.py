class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        def backtrack(node,temp):
            if node == None:
                return 
            if node.left == None and node.right == None:
                temp += str(node.val)
                output.append(temp)
                return
            temp += str(node.val) + '->'
            backtrack(node.left,temp)
            backtrack(node.right,temp)
        backtrack(root,"")
        return output
