class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def invert(i):
            i.left, i.right = i.right, i.left
            
            if i.left:
                invert(i.left)
            
            if i.right:
                invert(i.right)
        
        invert(root)

        return root
