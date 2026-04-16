# https://leetcode.com/problems/climbing-stairs/submissions/1978394255/

# 70. Climbing Stairs
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        print("Climbing...")
        climbs = []
        for i in range(0,n):
            if i==0:
                climbs.append(1)
            elif i ==1:
                climbs.append(2)
            else:
                climbs.append(climbs[i-1]+climbs[i-2])
        print(climbs)
        return climbs[-1]

Solution().climbStairs(3)
Solution().climbStairs(4)