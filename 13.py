class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        s_arr = list(s)
        # s_arr = ['I', 'V']
        print(s_arr)

        s_integers = []
        for i, rom in enumerate(s_arr):
            s_integers.append(dictionary[rom])
        # s_integers = [1, 5]
        print(s_integers)

        for i, num in enumerate(s_integers):
            if (i+1) < len(s_integers) and num < s_integers[i+1]:
                s_integers[i] = s_integers[i+1]
                s_integers[i+1] = -num
        # s_integers = [5, -1]
        print(s_integers)

        return(sum(s_integers))



sol = Solution()
print(sol.romanToInt("IV"))


# AI optimal ----------------------

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         total = 0
#         for i in range(len(s)):
#             if i + 1 < len(s) and dictionary[s[i]] < dictionary[s[i + 1]]:
#                 total -= dictionary[s[i]]
#             else:
#                 total += dictionary[s[i]]

#         return total