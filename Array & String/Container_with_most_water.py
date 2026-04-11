# https://leetcode.com/problems/container-with-most-water/submissions/1975155273/?envType=problem-list-v2&envId=array
# 11. Container With Most Water
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_areas , curr_area , left = 0,0,0
        right = len(height)-1

        while left < right:
            curr_area = min(height[left],height[right]) * (right-left)
            if height[left]< height[right]:
                left +=1
            else: 
                right -=1
            max_areas = max(curr_area,max_areas)
        return max_areas
    

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))