from src.load_data import load_data
from src.clean_data import clean
import plotly.express as px
import streamlit as st
from src.analysis import get_country_data 

df = clean(load_data())


year = st.slider("Select Year", int(df["year"].min()), int(df["year"].max()), int(df["year"].max()))
country1 = st.selectbox("Select country 1: ", df["country"].unique())
country2 = st.selectbox("Select country 2: ", df["country"].unique())


metric_selector = st.selectbox("Select Metric", ["life_ladder","gdp_per_capita","social_support","health","freedom","generosity","corruption"])
compared_countries = get_country_data(country1,country2,year,df)


bar_chart = px.bar(compared_countries,"country",metric_selector) # ,error_y_minus="lower_ci",error_y="upper_ci")
st.plotly_chart(bar_chart,use_container_width=True)




