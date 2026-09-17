class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start = 0
        cur = 0
        zeros = 0
        longest = 0
        while cur < len(nums):
            if nums[cur] == 0:
                zeros += 1

            while zeros > k and start < len(nums):
                if nums[start] == 0:
                    zeros -= 1
                start += 1


            if cur - start + 1> longest:
                longest = cur - start + 1

            cur += 1
        return longest 
