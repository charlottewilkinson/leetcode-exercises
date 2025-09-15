class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for start in range(len(s)-i+1):
                substr = s[start:start+i]
                half = len(substr) // 2
                if all(substr[j] == substr[-(j+1)] for j in range(half)):
                    return substr
                
        return ""

s = Solution()
print(s.longestPalindrome("a"))