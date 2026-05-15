# 197. Rising Temperature
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Weather

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# There are no different rows with the same recordDate.
# This table contains information about the temperature on a certain day.
 

# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Weather table:
# +----+------------+-------------+
# | id | recordDate | temperature |
# +----+------------+-------------+
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |
# +----+------------+-------------+
# Output: 
# +----+
# | id |
# +----+
# | 2  |
# | 4  |
# +----+
# Explanation: 
# In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
# In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate',ascending=True,inplace=True)
    weather['pre_date'] = weather['recordDate'].shift(1)
    weather['pre_tem'] = weather['temperature'].shift(1)
    final_df = weather[
        (weather['temperature'] > weather['pre_tem'])  &
        ((weather['recordDate'] - weather['pre_date']).dt.days == 1)
    ][['id']]
    breakpoint()
    return final_df


weather = pd.DataFrame({
    'id':[1,2,3,4],
    "recordDate" : pd.to_datetime(['2015-01-01','2015-01-02','2015-01-03','2015-01-04']),
    "temperature" : [10,25,20,30]
})

weather = pd.DataFrame({
    'id':[1,2],
    "recordDate" : pd.to_datetime(['2015-12-16','2015-12-15']),
    "temperature" : [3,-1]
})

print(rising_temperature(weather=weather))