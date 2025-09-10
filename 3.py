class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        count = 0
        longest = 0
        for start in range(len(s)):
            for i in range(len(s)-start):
                if s[start+i] not in seen:
                    seen.append(s[start])
                    count += 1
                else:
                    longest = max(longest, count)
            count = 0
            seen = []
        return longest


sol = Solution()
print(sol.lengthOfLongestSubstring("au"))