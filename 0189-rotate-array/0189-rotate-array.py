class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n  = [0]*len(nums)
        for i in range(0,len(nums)):
            n[(i+k) % len(nums)] = nums[i]
        for j in range(0,len(nums)):
            nums[j] = n[j]