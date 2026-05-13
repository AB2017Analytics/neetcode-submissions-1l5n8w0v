class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_lst = []
        for i in nums:
            if i in new_lst:
                return True
            else:
                new_lst.append(i)
        return False