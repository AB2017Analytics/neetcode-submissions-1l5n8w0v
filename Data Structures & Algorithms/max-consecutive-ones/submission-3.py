class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = cnt = 0
        for n in nums:
            cnt += 1 if n else -cnt
            r = max(r, cnt)
        return  r       