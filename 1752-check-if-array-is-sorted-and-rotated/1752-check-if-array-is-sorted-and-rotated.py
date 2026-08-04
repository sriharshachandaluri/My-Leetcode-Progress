class Solution:
    def check(self, nums: List[int]) -> bool:
        inp = nums+nums
        l = len(inp)
        for i in range(0,len(nums)):
            if inp[i:i+len(nums)] == sorted(inp[i:i+len(nums)]):
                return True
        return False