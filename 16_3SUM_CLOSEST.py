from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []
        n = len(nums)
        
        for i in range(n - 3):  # First pointer
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for nums[i]
                continue
            for j in range(i + 1, n - 2):  # Second pointer
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for nums[j]
                    continue
                
                left, right = j + 1, n - 1  # Two-pointer approach for the remaining part
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Move pointers and avoid duplicates
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        
                    elif current_sum < target:
                        left += 1  # Increase sum
                    else:
                        right -= 1  # Decrease sum
        
        return result
