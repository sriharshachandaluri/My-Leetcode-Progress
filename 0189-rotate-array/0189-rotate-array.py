class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(0,k):
            a = nums.pop()
            nums.insert(0,a)