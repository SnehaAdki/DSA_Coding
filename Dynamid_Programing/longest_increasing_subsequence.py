# 516. Longest Palindromic Subsequence
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)
        
        # Space optimized: use two 1D arrays instead of 2D
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            # Swap: current becomes previous for next iteration
            prev, curr = curr, prev
        
        return prev[n]


print(Solution().longestPalindromeSubseq(s="bbbab"))  # Output: 4