from typing import List

# TOO SLOW

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         for i in range(len(height)-1):
#             for j in range(i+1, len(height)):
#                 current_height = height[i] if height[i] <= height[j] else height[j]
#                 area = (j-i) * current_height
#                 if area > max_area:
#                     max_area = area
#         return max_area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            current_height = min(height[i], height[j])
            max_area = max(max_area, (j- i) * current_height)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))