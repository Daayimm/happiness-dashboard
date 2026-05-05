from src.load_data import load_data
from src.clean_data import clean
import plotly.express as px
from src.analysis import get_country_trends 
import streamlit as st

df = clean(load_data())

country = st.selectbox("Select a couuntry: ", df["country"].unique())
metrics = st.selectbox("Select a metrix to see its trend" ,  ["life_ladder","gdp_per_capita","social_support","health","freedom","generosity","corruption"])
country_trend = get_country_trends(country,df)


line_graph = px.line(country_trend,"year",metrics)


st.plotly_chart(line_graph,use_container_width=True)


