from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if closest == None or abs(total - target) < abs(closest - target):
                    closest = total
                    
                if total < target:
                    # if sum is too small, increase sum by moving left pointer
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total > target:
                    # if sum is too big, decrease sum by moving right pointer
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                else:
                    return target
        return closest



s = Solution()
print(s.threeSumClosest(nums = [0,1,2], target = 3))