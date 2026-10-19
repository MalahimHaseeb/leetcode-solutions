class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if not root.left:
            return root.right
        
        if not root.right:
            return root.left
        
        smallest = root.right

        while smallest.left:
            smallest = smallest.left

        smallest.left = root.left
        return root.right
        
