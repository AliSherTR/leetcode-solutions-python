from typing import List
# the condition is that the given array is sorted and we have to find the index for the target in O(log n)


################################################## BRUTE FORCE #########################################

# time complexity: O(n)

def searchInsert(nums: List[int] , target: int) -> int:
    for i in range(len(nums)):
        if(nums[i] >= target):
            return i
    return len(nums)

# print(searchInsert([1,3,5,6], 5))

################################################## OPTIMIZED SOLUTION #########################################
# method name : binary search
# time complexity: O(log n)

class Solution: 
    def searchInsert(self, nums: List[int] , target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return left
s = Solution()
print(s.searchInsert([1,3,5,6], 7))


################################################## RECURSIVE SOLUTION #########################################
# method name : binary search
# time complexity: O(log n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        def binary_search(left: int, right: int) -> int:
            # Base case: when the range is exhausted, return the insertion point
            if left > right:
                return left
            mid = (left + right) // 2  # Find the middle index
            if nums[mid] == target:
                return mid  # If target is found, return the index
            elif nums[mid] < target:
                return binary_search(mid + 1, right)  # Search in the right half
            else:
                return binary_search(left, mid - 1)  # Search in the left half
        
        # Start the recursive search from the full range of the list
        return binary_search(0, len(nums) - 1)
s = Solution()
print(s.searchInsert([1,3,5,6], 7))