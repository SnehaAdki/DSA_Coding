# https://leetcode.com/problems/subarray-sum-equals-k/submissions/1975171003/?envType=problem-list-v2&envId=array
# 560. Subarray Sum Equals K
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = {0: 1}  # Empty prefix has sum 0
        
        for num in nums:
            prefix_sum += num
            # If (prefix_sum - k) exists, those many subarrays end here with sum k
            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]
            # Record this prefix_sum
            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
        
        return count
    
Solution().subarraySum(nums = [1,2,3], k = 3)