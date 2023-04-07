class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        temp = root
        def insert(root, key):
            if root is None:
                return TreeNode(key)
            else:
                if root.val < key:
                    root.right = insert(root.right, key)
                else:
                    root.left = insert(root.left, key)
            return root
        for i in range(1, len(preorder)):
            insert(root, preorder[i])
        return root
