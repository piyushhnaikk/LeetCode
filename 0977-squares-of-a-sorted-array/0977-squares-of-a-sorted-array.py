class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        f_right = len(nums) - 1
        f_list = nums.copy()

        while left <= right:
            if nums[left] ** 2 >= nums [right] ** 2:
                f_list[f_right] = nums[left]**2
                left += 1
            else:
                f_list[f_right] = nums[right]**2
                right -= 1
            f_right -= 1

        return f_list