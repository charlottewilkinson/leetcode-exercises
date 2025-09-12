from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        unique_numbers = []
        blanks = []
        while index < len(nums):
            if nums[index] in unique_numbers:
                blanks.append("_")
                nums.remove(nums[index])
            else:
                unique_numbers.append(nums[index])
                index += 1

        nums += blanks
        return len(unique_numbers)
    
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))