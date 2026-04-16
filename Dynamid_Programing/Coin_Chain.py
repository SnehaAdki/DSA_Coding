# https://leetcode.com/problems/coin-change/submissions/1978490353/

# 322. Coin Change
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

from typing import List
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0 :
            return 0
        
        amount_arr = [0]*(amount+1)

        for i in range(1,len(amount_arr)):
            amount_arr[i] = sys.maxsize
            for coin in coins:
                if coin <= i and amount_arr[i-coin] != sys.maxsize:
                    amount_arr[i] = min(amount_arr[i],1+amount_arr[i-coin])

        if amount_arr[amount] == sys.maxsize:
            return -1
        return amount_arr[amount]
    
coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins,amount))