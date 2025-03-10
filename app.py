import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config for a wide layout
st.set_page_config(page_title="Bad Dashboard", layout="wide")

st.title("Bad Looking SuperStore Dashboard (Compact Layout)")

# Load dataset (adjust path as needed)
df = pd.read_excel("Sample - Superstore.xlsx")

# -- One Filter: Region --
regions = df["Region"].unique().tolist()
selected_region = st.selectbox("Select Region", ["All"] + regions)
if selected_region != "All":
    df = df[df["Region"] == selected_region]

# Show a small sample of the data
st.write("Here are the first 3 rows of the filtered data:")
st.dataframe(df.head(3))

# ----- Prepare Data for Charts -----
# Chart 1: Bar (Sales by Category)
category_sales = df.groupby("Category")["Sales"].sum().reset_index()

# Chart 2: Scatter (Sales vs Profit)
sales = df["Sales"]
profit = df["Profit"]

# Chart 3: Line (Sales Over Time)
if "Order Date" in df.columns:
    df_sorted = df.sort_values("Order Date")
    sales_over_time = df_sorted.groupby("Order Date")["Sales"].sum().reset_index()
else:
    sales_over_time = pd.DataFrame(columns=["Order Date", "Sales"])

# Chart 4: Bar (Profit by Sub-Category)
profit_subcat = df.groupby("Sub-Category")["Profit"].sum().reset_index()

# ----- Build Figures with Smaller Sizes -----
# Chart 1
fig1, ax1 = plt.subplots(figsize=(4, 3))
bar_colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
ax1.bar(category_sales["Category"], category_sales["Sales"], color=bar_colors[:len(category_sales)])
ax1.set_title("Sales by Category", color="#FF1493", fontsize=12)

# Chart 2
fig2, ax2 = plt.subplots(figsize=(4, 3))
ax2.scatter(sales, profit, color="#FF4500")
ax2.set_title("Sales vs Profit", color="#7FFF00", fontsize=12)
ax2.set_xlabel("Sales", color="#FFD700")
ax2.set_ylabel("Profit", color="#FFD700")

# Chart 3
fig3, ax3 = plt.subplots(figsize=(4, 3))
if not sales_over_time.empty:
    ax3.plot(sales_over_time["Order Date"], sales_over_time["Sales"], color="#00CED1")
    ax3.set_title("Sales Over Time", color="#FF69B4", fontsize=12)
    ax3.set_xlabel("Order Date", color="#00FF7F")
    ax3.set_ylabel("Sales", color="#00FF7F")
    plt.xticks(rotation=45)
else:
    ax3.text(0.5, 0.5, "No Order Date data available", ha="center", va="center")

# Chart 4
fig4, ax4 = plt.subplots(figsize=(4, 3))
ax4.barh(profit_subcat["Sub-Category"], profit_subcat["Profit"], color="#FF6347")
ax4.set_title("Profit by Sub-Category", color="#FF1493", fontsize=12)
ax4.set_xlabel("Profit", color="#FF1493")
ax4.set_ylabel("Sub-Category", color="#FF1493")

# ----- Arrange Charts in 2x2 Grid -----
col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)
    st.pyplot(fig2)

with col2:
    st.pyplot(fig3)
    st.pyplot(fig4)
