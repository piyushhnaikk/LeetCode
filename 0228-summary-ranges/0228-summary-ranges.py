class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst = []
        start = 0

        for i in range(1, len(nums) + 1 ):
            if  i == len(nums)  or nums[i] - 1 != nums[i - 1]:
                if start == i - 1:
                    lst.append(str(nums[start]))

                
                else:
                    lst.append(str(nums[start])  + "->" + str(nums[i - 1]))

                start = i
        return lst