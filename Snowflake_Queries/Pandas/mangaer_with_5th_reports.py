# 570. Managers with at Least 5 Direct Reports
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of an employee, their department, and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themself.
 

# Write a solution to find managers with at least five direct reports.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +-----+-------+------------+-----------+
# | id  | name  | department | managerId |
# +-----+-------+------------+-----------+
# | 101 | John  | A          | null      |
# | 102 | Dan   | A          | 101       |
# | 103 | James | A          | 101       |
# | 104 | Amy   | A          | 101       |
# | 105 | Anne  | A          | 101       |
# | 106 | Ron   | B          | 101       |
# +-----+-------+------------+-----------+
# Output: 
# +------+
# | name |
# +------+
# | John |
# +------+

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    val = employee.groupby(by = ['managerId']).agg(count = ('managerId' , 'count')).reset_index()
    exact = val.merge(employee , how='iner',left_on='managerId' , right_on='id')
    final = exact[exact['count']>=5]
    return final[['name']]


employee = pd.DataFrame({
    "id":[101,102,103,104,105,106],
    "name" : ['John','Dan','James','Amy','Anne','Ron'],
    "department" : ['A','A','A','A','A','B'],
    "managerId" : [None , 101,101,101,101,101]
})
print(find_managers(employee))