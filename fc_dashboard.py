import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Top Football Clubs Dashboard", layout="wide")
st.title("🏆 Football Clubs Insights Dashboard ⚽️")

uploaded_file = st.file_uploader("Upload your CSV file 👇", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # Sidebar Filters
    st.sidebar.header("🔍 Filters")
    countries = df["Country"].unique()
    selected_country = st.sidebar.multiselect("Select Country", options=countries, default=countries)

    filtered_df = df[df["Country"].isin(selected_country)]

    # KPIs
    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Revenue (B USD)", f"{filtered_df['Revenue (in Billion USD)'].mean():.2f}")
    col2.metric("Average Club Value (B USD)", f"{filtered_df['Club Value (in Billion USD)'].mean():.2f}")
    col3.metric("Average Stadium Capacity", f"{filtered_df['Stadium Capacity'].mean():.0f}")

    st.subheader("💵 Revenue by Club")
    fig1 = px.bar(filtered_df, x="Club", y="Revenue (in Billion USD)", color="Country",
    template="plotly_white")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📈 Club Values")
    fig2 = px.line(filtered_df, x="Club", y="Club Value (in Billion USD)", markers=True,
                   color="Country", template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🌍 Clubs per Country")
    country_counts = filtered_df["Country"].value_counts().reset_index()
    country_counts.columns = ["Country", "Count"]
    fig3 = px.pie(country_counts, names="Country", values="Count",)
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("🏟️ Stadium Capacity")
    fig4 = px.scatter(filtered_df, x="Club", y="Stadium Capacity", color="Country",
                      size="Stadium Capacity", hover_name="Club", template="plotly_white")
    st.plotly_chart(fig4, use_container_width=True)
