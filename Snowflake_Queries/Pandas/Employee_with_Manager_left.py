# 1978. Employees Whose Manager Left the Company
# Attempted
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Employees

# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | name        | varchar  |
# | manager_id  | int      |
# | salary      | int      |
# +-------------+----------+
# In SQL, employee_id is the primary key for this table.
# This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null). 
 

# Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

# Return the result table ordered by employee_id.

# The result format is in the following example.

 

# Example 1:

# Input:  
# Employees table:
# +-------------+-----------+------------+--------+
# | employee_id | name      | manager_id | salary |
# +-------------+-----------+------------+--------+
# | 3           | Mila      | 9          | 60301  |
# | 12          | Antonella | null       | 31000  |
# | 13          | Emery     | null       | 67084  |
# | 1           | Kalel     | 11         | 21241  |
# | 9           | Mikaela   | null       | 50937  |
# | 11          | Joziah    | 6          | 28485  |
# +-------------+-----------+------------+--------+
# Output: 
# +-------------+
# | employee_id |
# +-------------+
# | 11          |
# +-------------+

# Explanation: 
# The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
# Kalel's manager is employee 11, who is still in the company (Joziah).
# Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.

import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    final_df = None
    employee_ids = set(employees["employee_id"])
    final_df =  employees[ (employees["manager_id"].notna()) & (employees['salary'] < 30000 )& (~employees["manager_id"].isin(employee_ids))][["employee_id"]].sort_values("employee_id")
    return final_df



employees = pd.DataFrame({
    'employee_id' : [3,12,13,1,9,11],
    'name' : ['Mila','Antonella' , 'Emery','Kalel','Mikaela','Joziah'],
    'manager_id' : pd.array([9,None,None,11,None,6] , dtype='Int64'),
    'salary': [60301,31000,67084,21241,50937,28485]
})
print(find_employees(employees))