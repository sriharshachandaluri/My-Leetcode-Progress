class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while target != nums[mid]:
            if target < nums[mid]:
                right = mid - 1
                mid = (left + right) // 2
            else:
                left = mid + 1
                mid = (left + right) // 2
            if left > right:
                return -1

        return mid