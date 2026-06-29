# 1251. Average Selling Price
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Prices

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | start_date    | date    |
# | end_date      | date    |
# | price         | int     |
# +---------------+---------+
# (product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the price of the product_id in the period from start_date to end_date.
# For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
 

# Table: UnitsSold

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | purchase_date | date    |
# | units         | int     |
# +---------------+---------+
# This table may contain duplicate rows.
# Each row of this table indicates the date, units, and product_id of each product sold. 
 

# Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Prices table:
# +------------+------------+------------+--------+
# | product_id | start_date | end_date   | price  |
# +------------+------------+------------+--------+
# | 1          | 2019-02-17 | 2019-02-28 | 5      |
# | 1          | 2019-03-01 | 2019-03-22 | 20     |
# | 2          | 2019-02-01 | 2019-02-20 | 15     |
# | 2          | 2019-02-21 | 2019-03-31 | 30     |
# +------------+------------+------------+--------+
# UnitsSold table:
# +------------+---------------+-------+
# | product_id | purchase_date | units |
# +------------+---------------+-------+
# | 1          | 2019-02-25    | 100   |
# | 1          | 2019-03-01    | 15    |
# | 2          | 2019-02-10    | 200   |
# | 2          | 2019-03-22    | 30    |
# +------------+---------------+-------+
# Output: 
# +------------+---------------+
# | product_id | average_price |
# +------------+---------------+
# | 1          | 6.96          |
# | 2          | 16.96         |
# +------------+---------------+
# Explanation: 
# Average selling price = Total Price of Product / Number of products sold.
# Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
# Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96


import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged = units_sold.merge(prices, on='product_id', how='left')
    valid_sales = merged[merged['purchase_date'].between(merged['start_date'], merged['end_date'])].copy()
    valid_sales['revenue'] = valid_sales['price'] * valid_sales['units']

    grouped = valid_sales.groupby('product_id', as_index=False)
    .agg(
        total_revenue=('revenue', 'sum'),
        total_units=('units', 'sum')
    )
    grouped['average_price'] = (grouped['total_revenue'] / grouped['total_units']).round(2)

    all_products = pd.DataFrame({'product_id': pd.unique(pd.concat([prices['product_id'], units_sold['product_id']]))})
    result = all_products.merge(grouped[['product_id', 'average_price']], on='product_id', how='left')
    result['average_price'] = result['average_price'].fillna(0).round(2)

    return result[['product_id', 'average_price']]



prices = pd.DataFrame({
     "product_id" : [1,1,2,2],
     "start_date" : pd.to_datetime(['2019-02-17' , '2019-03-01' , '2019-02-01','2019-02-21']) , 
     "end_date" : pd.to_datetime(['2019-02-28' , '2019-03-22' , '2019-02-20','2019-03-31']) , 
     "price" : [5,20,15,30]
})


units = pd.DataFrame({
    "product_id" : [1,1,2,2],
    "purchase_date" : pd.to_datetime(['2019-02-25' ,'2019-03-01' , '2019-02-10' , '2019-03-22' ]),
    "units" : [100,15,200,30]
})

average_selling_price(prices,units)