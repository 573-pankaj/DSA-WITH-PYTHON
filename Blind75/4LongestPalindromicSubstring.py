class Solution(object):
    def longestPalindrome(self, s):
        
        # :type s: str
        # :rtype: str
# Every palindrome can be expanded from its center, and there are 2n - 1 such centers.
# You might be asking why there are 2n - 1 but not n centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even lengths."""
# a   b   c   d   e
# |   |   |   |   |       ← 5 character centers

#   |   |   |   |
#   ↑   ↑   ↑   ↑         ← 4 gap centers

        start = 0
        max_length = 1

        for i in range(len(s)):

            # Odd-length palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1

                left -= 1
                right += 1

            # Even-length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1

                left -= 1
                right += 1

        return s[start:start + max_length]