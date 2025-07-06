class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        result = 0

        for i in range(len(digits)):
            result = result + digits[i] * (10 ** i)

        result = result + 1
        result = list(str(result))

        for i in range(len(result)):
            result[i] = int(result[i])


        return result
