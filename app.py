import streamlit as st
import pandas as pd
from utils.categorisation import categorise_transaction
import plotly.express as px
from utils.subscriptions import detect_subscriptions


st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")

st.title("💳 Personal Finance Dashboard")

uploaded_file = st.file_uploader("Upload your transactions CSV", type=["csv"])

if uploaded_file:
    # 1. Load CSV
    df = pd.read_csv(uploaded_file)

    # 2. Convert date column + extract month
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["month"] = df["date"].dt.to_period("M").astype(str)

    # 3. Categorise transactions
    df["category"] = df["description"].apply(categorise_transaction)

    # 4. Layout: Two columns
    col1, col2 = st.columns([1.2, 1])

    # LEFT COLUMN — Tables
    with col1:
        st.write("### Raw Transactions")
        st.dataframe(df, use_container_width=True)

        st.write("### Categorised Transactions")
        st.dataframe(df, use_container_width=True)

    # RIGHT COLUMN — Category Spending Chart
    with col2:
        st.write("### Spending by Category")

        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        category_totals = df.groupby("category")["amount"].sum().reset_index()
        category_totals["spending"] = category_totals["amount"].abs()

        fig = px.bar(
            category_totals,
            x="category",
            y="spending",
            title="Total Spending by Category",
            color="category",
        )
        st.plotly_chart(fig, use_container_width=True)

    # FULL-WIDTH SECTION — Monthly Cashflow
    st.write("### Monthly Cashflow (Income vs Spending)")

    monthly = df.groupby("month")["amount"].sum().reset_index()
    monthly["income"] = monthly["amount"].apply(lambda x: x if x > 0 else 0)
    monthly["spending"] = monthly["amount"].apply(lambda x: abs(x) if x < 0 else 0)

    fig2 = px.bar(
        monthly,
        x="month",
        y=["income", "spending"],
        barmode="group",
        title="Monthly Income vs Spending",
    )
    st.plotly_chart(fig2, use_container_width=True)

    # 7. Subscription Detection
    st.write("### 🔁 Subscription Detection")

    subs = detect_subscriptions(df)

    if subs.empty:
     st.info("No recurring subscriptions detected.")
    else:
     st.dataframe(subs, use_container_width=True)


else:
    st.info("Upload a CSV file to begin.")
