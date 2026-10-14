class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return
            
            if depth == len(result):
                result.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth+1)
        
        dfs(root,0)
        return result
        
