from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the end of nums1 and nums2
        p1 = m - 1  # pointer for nums1 (last element of nums1)
        p2 = n - 1  # pointer for nums2 (last element of nums2)
        p = m + n - 1  # pointer for the last element in the merged array

        # While there are elements to compare in nums2
        while p1 >= 0 and p2 >= 0:
            # Place the larger element at the end of nums1
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them over
        # No need to copy nums1, as they are already in place
        nums1[:p2 + 1] = nums2[:p2 + 1]

        """
        Do not return anything, modify nums1 in-place instead.
        """
        