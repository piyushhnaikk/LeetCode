class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower = 0 
        if len(flowerbed) == 1:
            return (flowerbed[0] == 0  and n <= 1) or (flowerbed[0] == 1  and n == 0)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 :
                if i == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    flower += 1
                elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    flower += 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    flower += 1

            if flower >= n:
                return True
        return False

                    