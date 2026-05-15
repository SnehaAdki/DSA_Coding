# 610. Triangle Judgement

# Table: Triangle

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# In SQL, (x, y, z) is the primary key column for this table.
# Each row of this table contains the lengths of three line segments.
 

# Report for every three line segments whether they can form a triangle.

# Return the result table in any order.

# The result format is in the following example.

# Example 1:

# Input: 
# Triangle table:
# +----+----+----+
# | x  | y  | z  |
# +----+----+----+
# | 13 | 15 | 30 |
# | 10 | 20 | 15 |
# +----+----+----+
# Output: 
# +----+----+----+----------+
# | x  | y  | z  | triangle |
# +----+----+----+----------+
# | 13 | 15 | 30 | No       |
# | 10 | 20 | 15 | Yes      |
# +----+----+----+----------+



import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    
    triangle['triangle'] = triangle.apply(
        lambda row:'Yes' if (row['x']+row['y'] > row['z'] and
                            row['x']+row['z'] > row['y'] and 
                            row['z']+row['y'] > row['x'])
                        else 'No',
        axis =1
    )
    return triangle

triangles = pd.DataFrame({
    "x":[13,10],
    "y":[15,20],
    "z":[30,15]
})

print(triangle_judgement(triangles))