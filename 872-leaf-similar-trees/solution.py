class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        arr1 = []
        arr2 = []

        self.getLeaves(root1, arr1)
        self.getLeaves(root2, arr2)

        return arr1 == arr2

    
    def getLeaves(self, root, leaves):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            leaves.append(root.val)
        
        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
