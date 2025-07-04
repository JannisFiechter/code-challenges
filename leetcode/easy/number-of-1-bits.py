class Solution:
    def hammingWeight(self, n: int) -> int:
        decimal = n
        counter = 0
        binary = bin(decimal)[2:]
        
        nums = list(binary)

        for num in nums:
            num = int(num)
            if num == 1:
                counter = counter + 1

        return counter