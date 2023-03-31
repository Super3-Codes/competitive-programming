class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root):
            if root is None:
                return None

            if root.val > val:
                return search(root.left)
            elif root.val < val:
                return search(root.right)
            else:
                return root

        result =  search(root)
        return result
