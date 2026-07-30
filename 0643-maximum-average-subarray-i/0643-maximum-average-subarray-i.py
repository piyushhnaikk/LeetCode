class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        Sum = 0

        for i in range (k) :
            Sum +=  nums[i]
        
        Max = Sum / k
 
        while right + 1 < len(nums) :

            Sum -= nums[left]
            Sum += nums[right + 1]

            
            if Max < Sum / k:

                Max = Sum / k

            left += 1
            right += 1
        return Max
