class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        
        if not s or n < k:
            return 0
        
        vowels = set('aeiou')

        current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels = current_vowels

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels +=1
            
            if s[i-k] in vowels:
                current_vowels -=1

            max_vowels = max(current_vowels, max_vowels)
        
        return max_vowels
        
