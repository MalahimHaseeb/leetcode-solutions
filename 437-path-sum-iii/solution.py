class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(node, curr):
            if not node:
                return 0
            
            curr += node.val

            count = prefix.get(curr-targetSum, 0)

            prefix[curr] = prefix.get(curr,0) + 1

            count += dfs(node.left, curr)
            count += dfs(node.right, curr)
            prefix[curr] -=1

            return count
        
        return dfs(root,0)
