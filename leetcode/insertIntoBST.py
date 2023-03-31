def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def insert(root,prev):
            if root is None :
                if prev is not None:
                    if val > prev.val:
                        prev.right = TreeNode(val)
                    else:
                        prev.left = TreeNode(val)
                else:
                    return TreeNode(val)
                return

            if root.val > val:
                prev = root
                insert(root.left,prev)
            elif root.val < val:
                prev = root
                insert(root.right,prev)
                
        insert(root,None)
        return root
