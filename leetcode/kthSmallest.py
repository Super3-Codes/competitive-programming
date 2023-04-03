class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            values.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return values[k-1]
