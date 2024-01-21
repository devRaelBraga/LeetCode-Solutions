class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = ''
        longest_substring = ''

        for i in range(len(s)):
            if s[i] not in current_substring:
                current_substring += s[i]
            else:
                current_substring = current_substring[current_substring.index(s[i]) + 1:] + s[i]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            
        return len(longest_substring)
