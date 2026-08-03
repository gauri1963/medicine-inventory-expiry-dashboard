# Basic Code (Single Sheet)
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Read Excel file
df = pd.read_excel("pharmacy_star_schema2.xlsx")

# Display first 5 rows
print(df.head())

# Read Specific Sheet
import pandas as pd

# Read Fact Table
fact_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Fact_Inventory")

# Read Dimension Tables
medicine_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Medicine")
supplier_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Supplier")
category_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Category")
warehouse_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Warehouse")

# Check data
print(fact_df.head())
print(medicine_df)
print(supplier_df)
print(category_df)
print(warehouse_df)

# Check All Sheet Names

import pandas as pd

file = pd.ExcelFile("pharmacy_star_schema2.xlsx")
print(file.sheet_names)

# step 1: load all sheets
import pandas as pd

fact_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Fact_Inventory")
medicine_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Medicine")
supplier_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Supplier")
category_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Category")
warehouse_df = pd.read_excel("pharmacy_star_schema2.xlsx", sheet_name="Dim_Warehouse")

print(fact_df.head())
print(medicine_df.head())
print(supplier_df.head())
print(category_df.head())
print(warehouse_df.head())
print(fact_df.info())

# step 2: First I analyzed the structure, null values, and duplicates
print(fact_df.info())
print(fact_df.isnull().sum())
print(fact_df.duplicated().sum())

# STEP 3: Data Cleaning

# handle The Null value
fact_df["Medicine_ID"].fillna("Unknown", inplace=True)
print(df)

# Remove duplicates
fact_df = fact_df.drop_duplicates()
print(df)
# I handled missing values and removed duplicates for data quality.

# 4.Correct the data formate
fact_df["Expiry_Date"] = pd.to_datetime(fact_df["Expiry_Date"])
fact_df["Manufacturing_Date"] = pd.to_datetime(fact_df["Manufacturing_Date"])
print(df)
print(fact_df)

# STEP 5: Expiry Logic

from datetime import datetime

today = datetime.today()

fact_df["Days_To_Expire"] = (fact_df["Expiry_Date"] - today).dt.days

fact_df["Expiry_Status"] = fact_df["Days_To_Expire"].apply(
    lambda x: "Expired" if x < 0 else
              "Expiring Soon" if x <= 30 else
              "Safe"
)
print(df)
print(fact_df)

# calculated days to expiry and classified medicines into expired, expiring soon, and

# STEP 6: Star Schema Join
merged_df = fact_df.merge(medicine_df, on="Medicine_ID", how="left") \
                   .merge(supplier_df, on="Supplier_ID", how="left") \
                   .merge(category_df, on="Category_ID", how="left") \
                   .merge(warehouse_df, on="Warehouse_ID", how="left")

print(merged_df.head())
# combined fact and dimension tables using joins to create a unified dataset

#STEP 7: Analysis
#Low Stock
low_stock = merged_df[merged_df["Stock_Quantity"] <= merged_df["Reorder_Level"]]
print(low_stock)

# Expiring Soon
expiring = merged_df[merged_df["Expiry_Status"] == "Expiring Soon"]
print(expiring)

# Expired
expired = merged_df[merged_df["Expiry_Status"] == "Expired"]
print(df)

# STEP 8: Final Data Save
merged_df.to_csv("final_pharmacy_data.csv", index=False)
print(df)

# 1. Data Describe as padans

import pandas as pd

# Data describe
print(fact_df.describe())

# Matplotlib to Visualization

# 1. Expiry Status

merged_df["Expiry_Status"].value_counts().plot(kind="bar")

plt.title("Expiry Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()
# This graph shows medicine expiry classification

#2. Low Stock Medicines

low_stock = merged_df[merged_df["Stock_Quantity"] <= merged_df["Reorder_Level"]]

low_stock["Medicine_Name"].value_counts().head(10).plot(kind="bar")

plt.title("Low Stock Medicines")
plt.xlabel("Medicine")
plt.ylabel("Count")
plt.show()

# 3. Category Wise Inventory

merged_df.groupby("Category_Name")["Stock_Quantity"].sum().plot(kind="bar")

import matplotlib.pyplot as plt
plt.title("Category Wise Inventory")
plt.xlabel("Category")
plt.ylabel("Total Stock")
plt.show()

# 4. Supplier Distribution (Pie Chart)

merged_df["Supplier_Name"].value_counts().plot(kind="pie", autopct='%1.1f%%')

import matplotlib.pyplot as plt
plt.title("Supplier Distribution")
plt.ylabel("")
plt.show()

#5. Expiry Trend (Line Chart)

merged_df.groupby("Expiry_Date").size().plot(kind="line")

import matplotlib.pyplot as plt
plt.title("Expiry Trend")
plt.xlabel("Expiry Date")
plt.ylabel("Number of Medicines")
plt.show()

#6.Stock Quantity Distribution
import matplotlib.pyplot as plt

merged_df["Stock_Quantity"].hist()

plt.title("Stock Quantity Distribution")
plt.xlabel("Stock Quantity")
plt.ylabel("Frequency")
plt.show()

import seaborn as sns
# 7.Box Plot (Outliers)
plt.figure()
sns.boxplot(data=merged_df, y="Stock_Quantity")
plt.title("Stock Outliers")
plt.show()

#MySql connect
from sqlalchemy import create_engine
import pandas as pd

# 🔹 MySQL connection details
# MySQL connection details
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Get MySQL credentials
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

# Check that variables were loaded
print("Username:", username)
print("Host:", host)
print("Database:", database)

engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}"
)

print("MySQL engine created successfully!")

#  Read your final CSV (Python se jo banaya tha)
df = pd.read_csv("final_pharmacy_data.csv")

#  Store data into MySQL table
df.to_sql(name="medicine_inventory", con=engine, if_exists="replace", index=False)

print("Data successfully stored in MySQL")


# Create MySQL connection
engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}"
)

print("MySQL engine created successfully!")