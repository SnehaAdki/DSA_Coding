# 577. Employee Bonus

# Table: Employee

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | empId       | int     |
# | name        | varchar |
# | supervisor  | int     |
# | salary      | int     |
# +-------------+---------+
# empId is the column with unique values for this table.
# Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
 

# Table: Bonus

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | empId       | int  |
# | bonus       | int  |
# +-------------+------+
# empId is the column of unique values for this table.
# empId is a foreign key (reference column) to empId from the Employee table.
# Each row of this table contains the id of an employee and their respective bonus.
 

# Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

# The employee has a bonus less than 1000.
# The employee did not get any bonus.
# Return the result table in any order.

# The result format is in the following example. 

# Input: 
# Employee table:
# +-------+--------+------------+--------+
# | empId | name   | supervisor | salary |
# +-------+--------+------------+--------+
# | 3     | Brad   | null       | 4000   |
# | 1     | John   | 3          | 1000   |
# | 2     | Dan    | 3          | 2000   |
# | 4     | Thomas | 3          | 4000   |
# +-------+--------+------------+--------+

# Bonus table:
# +-------+-------+
# | empId | bonus |
# +-------+-------+
# | 2     | 500   |
# | 4     | 2000  |
# +-------+-------+

# Output: 
# +------+-------+
# | name | bonus |
# +------+-------+
# | Brad | null  |
# | John | null  |
# | Dan  | 500   |
# +------+-------+

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(bonus,how='left',on='empId')
    final_df = merged_df[(merged_df['bonus'] < 1000) | (merged_df['bonus'].isna())][['name','bonus']]
    breakpoint()
    return final_df

Employee = pd.DataFrame({'empId':[1,2,3,4],'name':['Brand','John','Dan','Thomas'],'supervisor':[None,3,3,3],'salary':[4000,1000,2000,4000]})
Bonus = pd.DataFrame({'empId':[2,4],'bonus':[500,2000]})

print(employee_bonus(Employee , Bonus))