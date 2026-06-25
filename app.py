import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="GitHub Trending Dashboard",
    layout="wide"
)

CSV_FILE = "data/trending.csv"

try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    st.error(
        "No data found. Run the scraper first."
    )
    st.stop()

st.title("GitHub Trending Dashboard")

# KPIs

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Repositories",
        df["repository"].nunique()
    )

with col2:
    st.metric(
        "Languages",
        df["language"].nunique()
    )

with col3:
    st.metric(
        "Average Stars",
        round(df["stars"].mean())
    )

st.divider()

# Top Languages

st.subheader("Top Languages")

language_count = (
    df["language"]
    .value_counts()
    .head(10)
)

fig_lang = px.bar(
    language_count,
    labels={
        "value": "Repositories",
        "index": "Language"
    }
)

st.plotly_chart(
    fig_lang,
    use_container_width=True
)

# Top Repositories

st.subheader("Top Repositories")

top_repos = (
    df.sort_values(
        by="stars",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_repos,
    use_container_width=True
)

# Evolution

st.subheader(
    "Daily Star Evolution"
)

daily = (
    df.groupby("date")["stars"]
    .mean()
    .reset_index()
)

fig_daily = px.line(
    daily,
    x="date",
    y="stars",
    markers=True
)

st.plotly_chart(
    fig_daily,
    use_container_width=True
)

# Ranking

st.subheader(
    "Interactive Ranking"
)

language = st.selectbox(
    "Select Language",
    sorted(
        df["language"]
        .dropna()
        .unique()
    )
)

filtered = df[
    df["language"] == language
]

filtered = filtered.sort_values(
    by="stars",
    ascending=False
)

st.dataframe(
    filtered,
    use_container_width=True
)