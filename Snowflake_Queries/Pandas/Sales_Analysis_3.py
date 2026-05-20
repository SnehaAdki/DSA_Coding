# 1084. Sales Analysis III
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Product

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# | unit_price   | int     |
# +--------------+---------+
# product_id is the primary key (column with unique values) of this table.
# Each row of this table indicates the name and the price of each product.
# Table: Sales

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | seller_id   | int     |
# | product_id  | int     |
# | buyer_id    | int     |
# | sale_date   | date    |
# | quantity    | int     |
# | price       | int     |
# +-------------+---------+
# This table can have duplicate rows.
# product_id is a foreign key (reference column) to the Product table.
# Each row of this table contains some information about one sale.
 

# Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Product table:
# +------------+--------------+------------+
# | product_id | product_name | unit_price |
# +------------+--------------+------------+
# | 1          | S8           | 1000       |
# | 2          | G4           | 800        |
# | 3          | iPhone       | 1400       |
# +------------+--------------+------------+
# Sales table:
# +-----------+------------+----------+------------+----------+-------+
# | seller_id | product_id | buyer_id | sale_date  | quantity | price |
# +-----------+------------+----------+------------+----------+-------+
# | 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
# | 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
# | 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
# | 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
# +-----------+------------+----------+------------+----------+-------+
# Output: 
# +-------------+--------------+
# | product_id  | product_name |
# +-------------+--------------+
# | 1           | S8           |
# +-------------+--------------+
# Explanation: 
# The product with id 1 was only sold in the spring of 2019.
# The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.
# The product with id 3 was sold after spring 2019.
# We return only product 1 as it is the product that was only sold in the spring of 2019.

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # Group by product and check if ALL sales are in Q1 2019
    sales_grouped = sales.groupby('product_id')['sales_date'].agg(['min', 'max'])
    
    # Find products where min >= 2019-01-01 AND max <= 2019-03-31
    q1_only = sales_grouped[
        (sales_grouped['min'] >= '2019-01-01') & 
        (sales_grouped['max'] <= '2019-03-31')
    ].reset_index()
    
    # Join with product table
    result = product[product['product_id'].isin(q1_only['product_id'])]

    return result[['product_id', 'product_name']]


product = pd.DataFrame({
    "product_id":[1,2,3],
    "product_name" : ['S8','G4' , 'iPhone'],
    "unit_price": [1000,800,1400]
})

sales = pd.DataFrame({
    "seller_id" : [1,1,2,3],
    "product_id" :[1,2,2,3],
    "buyer_id": [1,2,3,4],
    "sales_date" : pd.to_datetime(["2019-01-21","2019-02-17","2019-06-02","2019-05-13"]),
    "quantity" : [2,1,1,2],
    "price" : [2000,800,800,1800]
})

print(sales_analysis(product,sales))
