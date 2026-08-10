class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        
        if not n:
            return False

        numString1 = str(n)
        numString2 = str(x)

        if numString1[0] == numString2:
            return False

        if numString2 in numString1:
            return True

        return False
