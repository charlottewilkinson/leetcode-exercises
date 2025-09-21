from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        
        p1 = 0
        p2 = 0
        merged_list = []

        while p1 + p2 < (n // 2) + 2:
            if p1 == len(nums1):
                merged_list += nums2[p2: (n // 2) + 1 - p1]
                break
            elif p2 == len(nums2):
                merged_list += nums1[p1: (n // 2) + 1 - p2]
                break
            elif nums1[p1] < nums2[p2]:
                merged_list.append(nums1[p1])
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                merged_list.append(nums2[p2])
                p2 += 1
            else:
                # nums1[p1] == nums2[p2]
                merged_list.append(nums1[p1])
                merged_list.append(nums2[p2])
                p1 += 1
                p2 += 1

        if n % 2 == 0:
            # even
            median = (merged_list[(n // 2)-1] + merged_list[n // 2]) / 2

        else:
            # odd
            median = merged_list[(n // 2)]

        return median



s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,2,4,5,6], nums2 = [3]))