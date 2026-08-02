class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        zeros = 0
        max_len = 0
        
        while end < len(nums):

            if nums[end] == 0:
                zeros += 1
    
                while  zeros > k and end < len(nums):
                    if nums[start] == 0:
                        zeros -= 1
                    start += 1
                        
            end += 1
            if  end - start > max_len:
                max_len = end - start    
        return max_len