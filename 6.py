class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        loop_nums = [i for i in range(0, numRows)]
        loop_nums += [i for i in range(numRows-2, 0, -1)]

        count = 0
        array = [""]*numRows
        while count < len(s):
            for i in loop_nums:
                array[i] += s[count]
                count += 1
                if count >= len(s):
                    break
        
        final_s = ""
        for subs in array:
            final_s += subs

        return final_s

sol = Solution()
print(sol.convert(s= "PAYPALISHIRING", numRows = 4))