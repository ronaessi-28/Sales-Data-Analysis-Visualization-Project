import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts.data_cleaning import load_and_clean_data

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📈 Superstore Sales Dashboard")

# Load and clean data
df = load_and_clean_data('data/superstore_sales.csv')

# Sidebar filter
region = st.sidebar.selectbox("Select Region", df['Region'].unique())

st.subheader(f"Sales in {region}")
filtered = df[df['Region'] == region]

# Category Sales
cat_sales = filtered.groupby('Category')['Sales'].sum().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(data=cat_sales, x='Category', y='Sales', ax=ax1)
ax1.set_title('Category-wise Sales')
st.pyplot(fig1)

# Sub-Category Profit
sub_profit = filtered.groupby('Sub-Category')['Profit'].sum().sort_values().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(data=sub_profit, y='Sub-Category', x='Profit', palette='coolwarm', ax=ax2)
ax2.set_title('Sub-Category Profit')
st.pyplot(fig2)
