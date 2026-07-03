-- 180. Consecutive Numbers
-- Medium
-- Topics
-- premium lock icon
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column starting from 1.
 

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output: 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.

with 
Logs (id,num) as (
select * from values 
(1,1),
(2,1),
(3,1),
(4,2),
(5,1),
(6,2),
(7,2) t (id,num)
),
cnt_each as (
select  *,
row_number() over(partition by num order by id) as g_num,
from Logs order by id
)
select distinct  num as ConsecutiveNums
from cnt_each
group by num, id-g_num 
HAVING COUNT(*) >= 3
;


-- # Write your MySQL query statement below
-- with cte as (
--     select num,
--     lead(num,1) over() num1,
--     lead(num,2) over() num2
--     from logs

-- )

-- select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2)