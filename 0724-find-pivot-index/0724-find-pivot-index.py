class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = 0
        pivot = 0

        for i in nums:
            r_sum += i

        while pivot < len(nums):
            r_sum -= nums[pivot]
            if l_sum == r_sum:
                return pivot
            l_sum += nums[pivot] 
            pivot += 1

        return -1 