class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return None

        head = root
        
        while head:
            if val == head.val:
                return head
            
            if val < head.val:
                head = head.left
            else:
                head = head.right
        
        return None
        
