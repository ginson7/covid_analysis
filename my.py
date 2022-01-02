import streamlit as st
import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 










st.title('Live Covid Analysis')

case_report_download= pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-data.csv")
case_report=case_report_download

st.sidebar.title("Live Covid Analysis")

option= st.sidebar.selectbox(
   'Select The Country Name?',
    case_report["Country"].unique()
    )
df= case_report[case_report["Country"]==option]
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("Made By. -Ginson Pallickal")


     
 



a = df["New_cases"]
b = df["Cumulative_cases"]
c = df["New_deaths"]
d = df["Cumulative_deaths"]
y = df["Date_reported"]
new_case_vs_deaths=df[["New_cases","New_deaths"]]
cumulative_case_vs_deaths=df[["Cumulative_cases","Cumulative_deaths"]]



# plot lines

chart_data = pd.DataFrame(a)
chart_data1= pd.DataFrame(b)
chart_data2= pd.DataFrame(c)
chart_data3= pd.DataFrame(d)




st.subheader('New cases')
aa=("Latest Report: "+str(a.iloc[-1]) + "      "+ "Date Reported:   "+str(y.iloc[-1])+"      "+ "One day Max:  "+ str(a.max()))
st.text(aa)


st.subheader('New deaths')
cc=("Latest Report: "+str(c.iloc[-1]) + "      "+ "Date Reported:   "+str(y.iloc[-1]))
st.text(cc)

new_cases = st.checkbox('Show New cases VS New Death')
if new_cases:
    st.line_chart(new_case_vs_deaths)



st.subheader('Cumulative cases')
bb=("Latest Report: "+str(b.iloc[-1]) + "      "+ "Date Reported:   "+str(y.iloc[-1]))
st.text(bb)


st.subheader('Cumulative Death')
dd=("Latest Report: "+str(d.iloc[-1]) + "      "+ "Date Reported:   "+str(y.iloc[-1]))
st.text(dd)


cumulative_cases = st.checkbox('Show Cumulative cases VS Cumulative Deaths')
if cumulative_cases:
    st.line_chart(cumulative_case_vs_deaths)















