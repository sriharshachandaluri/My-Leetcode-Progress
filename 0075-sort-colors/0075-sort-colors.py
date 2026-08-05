class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = nums.count(0)
        j = nums.count(1)
        k = nums.count(2)
        for l in range(0,len(nums)):
            if i:
                nums[l] = 0
                i -= 1
            elif j:
                nums[l] = 1
                j -= 1
            elif k:
                nums[l] = 2
                l -= 1
        
