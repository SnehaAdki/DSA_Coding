# 1407. Top Travellers
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Users

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# id is the column with unique values for this table.
# name is the name of the user.
 

# Table: Rides

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | user_id       | int     |
# | distance      | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# user_id is the id of the user who traveled the distance "distance".
 

# Write a solution to report the distance traveled by each user.

# Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Users table:
# +------+-----------+
# | id   | name      |
# +------+-----------+
# | 1    | Alice     |
# | 2    | Bob       |
# | 3    | Alex      |
# | 4    | Donald    |
# | 7    | Lee       |
# | 13   | Jonathan  |
# | 19   | Elvis     |
# +------+-----------+
# Rides table:
# +------+----------+----------+
# | id   | user_id  | distance |
# +------+----------+----------+
# | 1    | 1        | 120      |
# | 2    | 2        | 317      |
# | 3    | 3        | 222      |
# | 4    | 7        | 100      |
# | 5    | 13       | 312      |
# | 6    | 19       | 50       |
# | 7    | 7        | 120      |
# | 8    | 19       | 400      |
# | 9    | 7        | 230      |
# +------+----------+----------+
# Output: 
# +----------+--------------------+
# | name     | travelled_distance |
# +----------+--------------------+
# | Elvis    | 450                |
# | Lee      | 450                |
# | Bob      | 317                |
# | Jonathan | 312                |
# | Alex     | 222                |
# | Alice    | 120                |
# | Donald   | 0                  |
# +----------+--------------------+
# Explanation: 
# Elvis and Lee traveled 450 miles, Elvis is the top traveler as his name is alphabetically smaller than Lee.
# Bob, Jonathan, Alex, and Alice have only one ride and we just order them by the total distances of the ride.
# Donald did not have any rides, the distance traveled by him is 0.


import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    grouped_val = rides.groupby(by=['user_id']).sum().reset_index()[['user_id','distance']]
    result = users.merge(grouped_val, how='left' , left_on='id', right_on='user_id').fillna({'distance':0})
    result['distance'] = result['distance'].astype(int)
    final_result = result[['name','distance']].rename(columns = {'distance' : 'travelled_distance'})
    return final_result.sort_values(['travelled_distance','name'],ascending=[False,True])


users = pd.DataFrame({
    "id" : [1,2,3,4,7,13,19],
    "name" :['Alice' , 'Bob' , 'Alex','Donald','Lee' , 'Jonathan','Elvis']
})

rides = pd.DataFrame({
    "id" :[1,2,3,4,5,6,7,8,9],
    "user_id" : [1,2,3,7,13,19,7,19,7],
    "distance" : [120,317,222,100,312,50,120,400,230]
})

print(top_travellers(users,rides))