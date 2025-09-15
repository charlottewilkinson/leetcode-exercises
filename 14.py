from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(len(s) for s in strs)

        prefix = []
        for i in range(shortest):
            ch = strs[0][i]
            if any(s[i] != ch for s in strs[1:]):
                break
            prefix.append(ch)
        return "".join(prefix)

s = Solution()
print(s.longestCommonPrefix(["caa","","a","acb"]))