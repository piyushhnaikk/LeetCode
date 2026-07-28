class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        
        index = 0
        for i in nums:
            if i in indices:
                if  index - indices[i]  <= k :
                    return True
                indices[i] = index
                
            else:
                indices[i] = index
            index += 1
        return False