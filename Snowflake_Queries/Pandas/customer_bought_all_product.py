# Accepted
# Accepted
# Editorial
# Editorial
# Solutions
# Solutions
# Submissions
# Submissions
# Code
# Testcase
# Testcase
# Test Result
# Leet
# 1045. Customers Who Bought All Products
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Customer

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | customer_id | int     |
# | product_key | int     |
# +-------------+---------+
# This table may contain duplicates rows. 
# customer_id is not NULL.
# product_key is a foreign key (reference column) to Product table.
 

# Table: Product

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_key | int     |
# +-------------+---------+
# product_key is the primary key (column with unique values) for this table.
 

# Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Customer table:
# +-------------+-------------+
# | customer_id | product_key |
# +-------------+-------------+
# | 1           | 5           |
# | 2           | 6           |
# | 3           | 5           |
# | 3           | 6           |
# | 1           | 6           |
# +-------------+-------------+
# Product table:
# +-------------+
# | product_key |
# +-------------+
# | 5           |
# | 6           |
# +-------------+
# Output: 
# +-------------+
# | customer_id |
# +-------------+
# | 1           |
# | 3           |
# +-------------+
# Explanation: 
# The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer['dense_rank'] = customer.groupby(by=['customer_id'])['product_key'].rank(method='dense').astype(int)
    print(customer)
    distinct_values = product['product_key'].count()
    customer_sorted = customer[customer['dense_rank']>=distinct_values]
    final_customer = customer_sorted['customer_id'].unique()
    # customer[['customer_id']]
    return pd.DataFrame({'customer_id' : final_customer})


customer = pd.DataFrame({
    "customer_id" : [1,2,3,3,1],
    "product_key" : [5,6,5,6,6]
})

Product = pd.DataFrame({
    "product_key" : [5,6]
})

print(find_customers(customer , Product))