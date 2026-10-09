class Solution:
    def goodNodes(self, root):
        def dfs(node, maximum):
            if not node:
                return 0

            count = 1 if node.val >= maximum else 0
            maximum = max(maximum, node.val)

            return count + dfs(node.left, maximum) + dfs(node.right, maximum)

        return dfs(root, root.val)
