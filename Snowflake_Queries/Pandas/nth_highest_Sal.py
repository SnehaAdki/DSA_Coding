# 177. Nth Highest Salary
# Medium
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# Example 2:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+


import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_sal = employee['salary'].drop_duplicates()

    sor_sal = unique_sal.sort_values(ascending=False)

    if N > len(sor_sal) or N <= 0: 
        return pd.DataFrame({f'getNthHighestSalary({N})' :[None]})
    
    nth_index = sor_sal.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})' :[nth_index]})


employee = pd.DataFrame({
    "id":[1,2,3],
    "salary" : [100,200,300]
})

print(nth_highest_salary(employee,1))