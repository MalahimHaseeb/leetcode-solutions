class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        n = len(vals)
        best = 0

        for i in range(n//2):
            best = max(best, vals[i] + vals[n-1-i])
        
        return best
