from typing import Dict, List

class Solution:
    DIGIT_TO_LETTERS = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        all_combs = []

        for d in digits:
            all_combs = self.createCombs(d, all_combs)
        
        return all_combs
    
    def createCombs(self, digit: str, all_combs: List[str]) -> List[str]:
        mapping = Solution.DIGIT_TO_LETTERS
        n = len(all_combs)
        
        if n == 0:
            for letter in mapping[digit]:
                all_combs += letter

            return all_combs
        
        else:
            new_combs = []
            for comb in range(n):
                for letter in mapping[digit]:
                    new_combs.append(all_combs[comb] + letter)

            return new_combs
        


s = Solution()
print(s.letterCombinations("2345"))