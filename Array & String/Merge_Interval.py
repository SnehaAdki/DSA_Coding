# https://leetcode.com/problems/merge-intervals/submissions/1973723583/?envType=problem-list-v2&envId=array
# 56. Merge Intervals
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Example 3:
# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        final_arr = []
        for i in range(0,len(intervals)):
            if not final_arr or final_arr[-1][-1] < intervals[i][0]:
                final_arr.append(intervals[i])
            else:
                final_arr[-1][1] = max(final_arr[-1][1] , intervals[i][1])

        return final_arr

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
print(Solution().merge(intervals))