class Solution:
    def removeDuplicates(self , nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[i -1]):
                nums[k] = nums[i]
                k = k + 1
        return k

s = Solution()
print(s.removeDuplicates([1 ,1 ,2]))