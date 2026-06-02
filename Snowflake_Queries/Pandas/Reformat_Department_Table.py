# 1179. Reformat Department Table
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Department

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | revenue     | int     |
# | month       | varchar |
# +-------------+---------+
# In SQL,(id, month) is the primary key of this table.
# The table has information about the revenue of each department per month.
# The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

# Reformat the table such that there is a department id column and a revenue column for each month.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Department table:
# +------+---------+-------+
# | id   | revenue | month |
# +------+---------+-------+
# | 1    | 8000    | Jan   |
# | 2    | 9000    | Jan   |
# | 3    | 10000   | Feb   |
# | 1    | 7000    | Feb   |
# | 1    | 6000    | Mar   |
# +------+---------+-------+
# Output: 
# +------+-------------+-------------+-------------+-----+-------------+
# | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
# +------+-------------+-------------+-------------+-----+-------------+
# | 1    | 8000        | 7000        | 6000        | ... | null        |
# | 2    | 9000        | null        | null        | ... | null        |
# | 3    | null        | 10000       | null        | ... | null        |
# +------+-------------+-------------+-------------+-----+-------------+
# Explanation: The revenue from Apr to Dec is null.
# Note that the result table has 13 columns (1 for the department id + 12 for the months).


import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    prefixes = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    bymonth = department.pivot_table(
        index='id',
        columns='month',
        values='revenue',
        aggfunc='sum'
    )
    bymonth = bymonth.reindex(columns=prefixes)
    bymonth.rename(columns = lambda prefix : prefix+"_Revenue" , inplace= True)
    bymonth.reset_index(inplace=True)
    return bymonth



department = pd.DataFrame({
    "id" : [1,2,3,1,1],
    "revenue": [8000,9000,10000,7000,6000],
    "month" : ['Jan' , 'Jan' , 'Feb' , 'Feb' , 'Mar']
})

print(reformat_table(department))