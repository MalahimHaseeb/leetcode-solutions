class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        self.best = 0

        def dfs(node, left, right):
            if not node:
                return 
            
            self.best = max(self.best, left, right)
            dfs(node.left, right+1 , 0)
            dfs(node.right, 0 , left  +1)
        
        dfs(root,0,0)

        return self.best
        
