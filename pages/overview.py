import streamlit as st
from src.load_data import load_data
from src.clean_data import clean
import plotly.express as px

df = clean(load_data())

year = st.slider("Select Year", int(df["year"].min()), int(df["year"].max()), int(df["year"].max()))
filtered = df[df["year"] == year]

st.subheader(f"Happiness Score by Country — {year}")

fig = px.choropleth(
    filtered,
    locations="country",
    locationmode="country names",
    color="life_ladder",
    color_continuous_scale="RdYlGn",
    title=f"World Happiness {year}",
    labels={"life_ladder": "Happiness Score"}
)
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    top = filtered.nlargest(10, "life_ladder")[["country", "life_ladder"]]
    st.subheader("Top 10 Happiest")
    st.dataframe(top, hide_index=True)
with col2:
    bottom = filtered.nsmallest(10, "life_ladder")[["country", "life_ladder"]]
    st.subheader("Bottom 10")
    st.dataframe(bottom, hide_index=True)