class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        elif n % 2 == 0:
            while n % 2 == 0:
                n = n // 2
            return n == 1

        elif n == 1:
            return True
            
        else:
            return False