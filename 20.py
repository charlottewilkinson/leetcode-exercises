class Solution:
    def isValid(self, s: str) -> bool:

        char_dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in char_dict.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != char_dict.get(c):
                    return False
        if stack:
            return False
        else:
            return True

s = Solution()
print(s.isValid("["))