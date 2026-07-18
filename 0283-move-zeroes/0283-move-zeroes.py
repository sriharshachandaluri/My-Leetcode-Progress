class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = nums.count(0)
        for i in range(j):
            nums.remove(0)
            nums.append(0)
        print(nums)    