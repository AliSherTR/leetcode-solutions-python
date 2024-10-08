from typing import List
class Solution:
    def plusOne(self, digits : List[int] ) -> List[int]:
        combined = int(''.join(map(str , digits)))
        combined = combined + 1
        split_list = []

        while combined > 0:
            digit = combined % 10
            split_list.insert(0 , digit)
            combined = combined // 10
        return split_list
    
s = Solution()
print(s.plusOne([1 ,2 ,3]))