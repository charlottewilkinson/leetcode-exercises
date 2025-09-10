class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_array = [int(d) for d in str(x)]
        for i in range(len(x_array)//2):
            if x_array[i] == x_array[-(i+1)]:
                continue
            else:
                return False
        return True
    
s = Solution()
print(s.isPalindrome(101))