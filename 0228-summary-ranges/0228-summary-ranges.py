class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        j = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                if i - j == 1:
                    result.append(str(nums[j]))
                else:
                    result.append(f"{nums[j]}->{nums[i - 1]}")
                j = i

        # Process the last range
        if len(nums) - j == 1:
            result.append(str(nums[j]))
        else:
            result.append(f"{nums[j]}->{nums[-1]}")

        return result