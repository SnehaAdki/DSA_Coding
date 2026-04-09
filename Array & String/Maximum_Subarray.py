# https://leetcode.com/problems/maximum-subarray/submissions/1973676813/?envType=problem-list-v2&envId=array

# 53. Maximum Subarray
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        m_s_f = nums[0]

        for i in range(1,len(nums)):
            curr_max = max(nums[i] , curr_max+nums[i])
            m_s_f = max(curr_max , m_s_f)

        return m_s_f
        
