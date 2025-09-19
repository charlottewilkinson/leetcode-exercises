# from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triples = []
#         nums.sort()
#         print(nums)
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if (i != j and 
#                         i != k and 
#                         j != k and 
#                         nums[i] + nums[j] + nums[k] == 0):
#                         new_triple = [nums[i], nums[j], nums[k]]
#                         if all(set(new_triple) != set(triple) for triple in triples):
#                             triples.append(new_triple)
#         return triples

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Since array is sorted, if anchor > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            target = -nums[i]
            l, r = i + 1, n - 1

            while l < r:
                print(i,l,r)
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates for l and r
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res


s = Solution()
print(s.threeSum([-4, -1, -1, 0, 1, 2]))