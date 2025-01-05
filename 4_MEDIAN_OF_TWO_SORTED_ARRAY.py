class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two arrays
        nums1.extend(nums2)  # Use extend instead of append to combine arrays
        nums1.sort()         # Sort the merged array

        n = len(nums1)
        
        # Check if the length of the array is odd or even
        if n % 2 == 0:  # If even
            mid1 = n // 2
            mid2 = mid1 - 1
            median = (nums1[mid1] + nums1[mid2]) / 2
        else:           # If odd
            mid = n // 2
            median = nums1[mid]
        
        return median
