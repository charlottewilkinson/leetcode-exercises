class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        count = 0
        longest = 0
        for start in range(len(s)):
            seen.append(s[start])
            count += 1
            longest = max(longest, count)
            for i in range(1, len(s)-start):
                if s[start+i] not in seen:
                    seen.append(s[start+i])
                    count += 1
                    longest = max(longest, count)
                else:
                    break
            
            seen = []
            count = 0
        return longest

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))