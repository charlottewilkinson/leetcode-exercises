from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                # skip duplicate ancors
                continue
            if nums[i] > 0:
                # cant get triples == 0 if i, l, and r are all > 0
                break

            l = i+1
            r = n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    # if sum is too small, increase sum by moving left pointer
                    l += 1
                    continue
                if total > 0:
                    # if sum is too big, decrease sum by moving right pointer
                    r -= 1
                    continue
                if total == 0:
                    triples.append([nums[i], nums[l], nums[r]])
                    left = nums[l]
                    right = nums[r]
                    # skip duplicate pointers
                    while nums[l] == left and l < r:
                        l += 1
                    while nums[r] == right and l < r:
                        r -= 1
        return triples



s = Solution()
print(s.threeSum([0, 0, 0]))