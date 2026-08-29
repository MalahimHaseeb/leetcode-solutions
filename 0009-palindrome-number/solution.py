class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != abs(x):
            return False
        
        if str(x) == str(x)[::-1]:
            return True

        return False
