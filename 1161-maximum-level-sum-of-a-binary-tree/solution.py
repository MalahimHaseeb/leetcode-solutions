class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        best = {}

        def dfs(node, level):
            if not node:
                return
            best[level] = best.get(level, 0) + node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return max(best, key=best.get)
