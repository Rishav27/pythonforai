import os
import pandas as pd
import json
from helper import calculate_total, formating_currency

#--------------------------------------------------
#reading data from csv file
df = pd.read_csv("data/sales.csv")


#--------------------------------------------------
#calculating total sales
total = []
for index, row in df.iterrows():
  totalAmount = calculate_total(row['quantity'], row['price'])
  total.append(totalAmount)

df['total'] = total


#--------------------------------------------------
#fromating the total amount in currency format
for index, row in df.iterrows():
  formating_total = formating_currency(row['total'])
  print(f"product: {row['product']}, total sales: {formating_total}")

#--------------------------------------------------

grandTotal = df['total'].sum()
formatingGrandTotal = formating_currency(grandTotal)
print(f'Grand Total Sales: {formatingGrandTotal}')