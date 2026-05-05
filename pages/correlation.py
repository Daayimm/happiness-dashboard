from src.load_data import load_data
from src.clean_data import clean
import plotly.express as px
import streamlit as st



df = clean(load_data())

metrics = st.selectbox("Select a metrix to see its trend" ,  ["gdp_per_capita","social_support","health","freedom","generosity","corruption"])

year = st.slider("Select Year", int(df["year"].min()), int(df["year"].max()), int(df["year"].max()))
filtered = df[df["year"] == year]

scatter_plot = px.scatter(filtered,"life_ladder",metrics,trendline="ols")

st.plotly_chart(scatter_plot,use_container_width=True)



