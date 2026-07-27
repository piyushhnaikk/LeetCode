class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        index = 0
        for i in nums:
            complement = target - i
            if complement in freq:
                return [freq[complement], index]
            if i in freq:
                freq[i] += index
            else:
                freq[i] = index
            index += 1
