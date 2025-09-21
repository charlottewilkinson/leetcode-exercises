class Solution:
    def reverse(self, x: int) -> int:
        list_x = list(str(x))
        new_x = ""

        if list_x[0] == "-":
            new_x += "-"
            list_x.remove("-")
        
        n = len(list_x)

        for i in range(n-1, -1, -1):
            new_x += list_x[i]
        
        new_x = int(new_x)

        if -2**31 <= new_x <= (2**31) - 1:
            return new_x
        else:
            return 0

s = Solution()
print(s.reverse(-2147483648))