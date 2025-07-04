class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = list(x)[::-1]
        y = ''.join(y)
        return x == y