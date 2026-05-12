-- 197. Rising Temperature
-- Solved
-- Easy
-- Topics
-- premium lock icon
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Weather

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the column with unique values for this table.
-- There are no different rows with the same recordDate.
-- This table contains information about the temperature on a certain day.
 

-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).


with 
Temperature_data(id,record_date,temperature) as (
    select * from values  
    (1,'2015-01-31'::DATE,10),
    (1,'2015-02-1'::DATE,25),
    (1,'2015-02-2'::DATE,20),
    (2,'2015-02-3'::DATE,30) 
    as t(id,record_date,temperature)
),
prev_val_temperature (id,rec_date,tem,pre_tem , prev_date) as (
select 
* ,
lag(Temperature_data.temperature) over(order by record_date ) as prev_temp,
lag(Temperature_data.record_date) over(order by record_date ) as prev_date
from Temperature_data ) 
select * from prev_val_temperature where tem > PRE_TEM and DATEDIFF(day,prev_date,rec_date)=1
;
