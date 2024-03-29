class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(root,result):
            if root == None:
                return 
            inorder(root.left,result)
            result.append(root.val)
            inorder(root.right,result)
        result = []
        inorder(root,result)
        return result
