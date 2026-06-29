
-- 1251. Average Selling Price
-- Solved
-- Easy
-- Topics
-- premium lock icon
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Prices

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | start_date    | date    |
-- | end_date      | date    |
-- | price         | int     |
-- +---------------+---------+
-- (product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
-- Each row of this table indicates the price of the product_id in the period from start_date to end_date.
-- For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
 

-- Table: UnitsSold

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | purchase_date | date    |
-- | units         | int     |
-- +---------------+---------+
-- This table may contain duplicate rows.
-- Each row of this table indicates the date, units, and product_id of each product sold. 
 

-- Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Prices table:
-- +------------+------------+------------+--------+
-- | product_id | start_date | end_date   | price  |
-- +------------+------------+------------+--------+
-- | 1          | 2019-02-17 | 2019-02-28 | 5      |
-- | 1          | 2019-03-01 | 2019-03-22 | 20     |
-- | 2          | 2019-02-01 | 2019-02-20 | 15     |
-- | 2          | 2019-02-21 | 2019-03-31 | 30     |
-- +------------+------------+------------+--------+
-- UnitsSold table:
-- +------------+---------------+-------+
-- | product_id | purchase_date | units |
-- +------------+---------------+-------+
-- | 1          | 2019-02-25    | 100   |
-- | 1          | 2019-03-01    | 15    |
-- | 2          | 2019-02-10    | 200   |
-- | 2          | 2019-03-22    | 30    |
-- +------------+---------------+-------+
-- Output: 
-- +------------+---------------+
-- | product_id | average_price |
-- +------------+---------------+
-- | 1          | 6.96          |
-- | 2          | 16.96         |
-- +------------+---------------+
-- Explanation: 
-- Average selling price = Total Price of Product / Number of products sold.
-- Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
-- Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

with 
prices (product_id, start_date,end_date,price ) as (
select * from values 
(1,'2019-02-17'::DATE , '2019-02-28'::DATE , 5),
(1,'2019-03-01'::DATE , '2019-03-22'::DATE , 20),
(2,'2019-02-01'::DATE , '2019-02-20'::DATE , 15),
(2,'2019-02-21'::DATE , '2019-03-31'::DATE , 30),
(3,'2019-03-22'::DATE,'2019-03-22'::DATE , 30) t (product_id, start_date,end_date,price ) 
),
unitssold (product_id,purchase_date,units) as (
select * from values 
(1,'2019-02-25'::DATE , 100),
(1,'2019-03-01'::DATE , 15),
(2,'2019-02-10'::DATE , 200),
(2,'2019-03-22'::DATE , 30)t (product_id,purchase_date,units)
),
effective_rec as (
select  --* from prices;
p.product_id,p.start_date,p.end_date,p.price,u.purchase_date,u.units,  ifNULL( (p.price * u.units) , 0) as product_unit_sum  from prices p
left join 
unitssold u
on p.product_id = u.product_id and (u.purchase_date>= p.start_date and u.purchase_date<=p.end_date) 
),

each_product_unit as (
select product_id,coalesce(sum(units),0) as total_units from effective_rec 
group by product_id
)

select final_res.product_id ,
       case when coalesce(final_res.total_units,0) = 0 then 0
            else round(coalesce(final_res.average_price,0)/final_res.total_units,2) end as average_price from (
select avg_total.product_id,avg_total.average_price,epu.total_units 
from (
select product_id , sum(product_unit_sum) as average_price from 
(
select er.product_id,ec.total_units,er.product_unit_sum from effective_rec er 
left join 
each_product_unit ec 
on er.product_id = ec.product_id ) e group by product_id)avg_total
left join 
each_product_unit epu
on avg_total.product_id = epu.product_id ) final_res
;
