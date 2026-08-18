class Solution:

    def hasDuplicate(self, nums: list[int]) -> bool:  # Added 'self'
        return len(nums) != len(set(nums))