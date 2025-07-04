class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []

        # Step 1: Find the length of the shortest word
        shortest_length = len(strs[0])
        for word in strs:
            if len(word) < shortest_length:
                shortest_length = len(word)

        # Step 2: Loop over each character index up to the shortest word length
        for i in range(shortest_length):
            current_char = strs[0][i]  # Take character from the first word

            # Step 3: Compare with all other words at the same index
            for word in strs:
                if word[i] != current_char:
                    # As soon as there's a mismatch, return what we've found
                    return ''.join(result)

            # If no mismatch, add character to result
            result.append(current_char)

        # Step 4: All characters matched up to shortest_length
        return ''.join(result)