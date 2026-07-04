class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_freq = 0
        result = 0

        for r in range(len(s)):
            # Add current character to the window
            count[s[r]] = 1 + count.get(s[r], 0)

            # Track the count of the most frequent character in the window
            max_freq = max(max_freq, count[s[r]])

            # Current window size
            window_len = r - l + 1

            # If replacements needed > k, shrink from the left
            if window_len - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # Update longest valid window length
            result = max(result, r - l + 1)

        return result