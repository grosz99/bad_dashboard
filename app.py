import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config for a full-width layout (optional)
st.set_page_config(page_title="Bad Dashboard", layout="wide")

st.title("Bad Looking SuperStore Dashboard")

# Load dataset from the data folder (ensure the file is here)
df = pd.read_excel("Sample - Superstore.xlsx")

# -------- One Filter: Region --------
regions = df["Region"].unique().tolist()
selected_region = st.selectbox("Select Region", ["All"] + regions)
if selected_region != "All":
    df = df[df["Region"] == selected_region]

st.write("Showing the first 5 rows of the filtered data:")
st.write(df.head())

# -------- Chart 1: Bar Chart --------
# Total Sales by Category with bright colors
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
fig1, ax1 = plt.subplots()
bar_colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
ax1.bar(category_sales["Category"], category_sales["Sales"], color=bar_colors[:len(category_sales)])
ax1.set_title("Sales by Category", color="#FF1493", fontsize=14)
st.pyplot(fig1)

# -------- Chart 2: Scatter Plot --------
# Scatter plot of Sales vs Profit with a bright color
fig2, ax2 = plt.subplots()
ax2.scatter(df["Sales"], df["Profit"], color="#FF4500")
ax2.set_title("Sales vs Profit", color="#7FFF00", fontsize=14)
ax2.set_xlabel("Sales", color="#FFD700")
ax2.set_ylabel("Profit", color="#FFD700")
st.pyplot(fig2)

# -------- Chart 3: Line Chart --------
# Line chart of Sales over Time using the Order Date
if "Order Date" in df.columns:
    df_sorted = df.sort_values("Order Date")
    sales_over_time = df_sorted.groupby("Order Date")["Sales"].sum().reset_index()
    fig3, ax3 = plt.subplots()
    ax3.plot(sales_over_time["Order Date"], sales_over_time["Sales"], color="#00CED1")
    ax3.set_title("Sales Over Time", color="#FF69B4", fontsize=14)
    ax3.set_xlabel("Order Date", color="#00FF7F")
    ax3.set_ylabel("Sales", color="#00FF7F")
    plt.xticks(rotation=45)
    st.pyplot(fig3)
else:
    st.write("Order Date column not found.")

# -------- Chart 4: Bar Chart for Profit by Sub-Category --------
# Replaces the pie chart to avoid negative wedge size issues
profit_subcat = df.groupby("Sub-Category")["Profit"].sum().reset_index()
fig4, ax4 = plt.subplots()
ax4.barh(profit_subcat["Sub-Category"], profit_subcat["Profit"], color="#FF6347")
ax4.set_title("Profit by Sub-Category", color="#FF1493", fontsize=14)
ax4.set_xlabel("Profit", color="#FF1493")
ax4.set_ylabel("Sub-Category", color="#FF1493")
st.pyplot(fig4)
