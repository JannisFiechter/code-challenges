class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        total = 0
        while i < len(s):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                # Subtractive case, like IV or IX
                total += roman[s[i+1]] - roman[s[i]]
                i += 2  # Skip the next character because we just used it
            else:
                # Normal case
                total += roman[s[i]]
                i += 1
        return total
 