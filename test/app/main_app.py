import streamlit as st
import pandas as pd 
import sys
import plot

st.title('Stat Tirs')



Championshipchoice = st.sidebar.selectbox("which Championship do you want ?",("Tirs_Bundesliga.csv","Tirs_PL.csv","Tirs_liga.csv","Tirs_SerieA.csv","Tirs_L1.csv") )


choice = "../data/" + Championshipchoice
TableChoice = pd.read_csv(choice)
ChampionshipName = choice.split(".")[2].split("_")[1]


figure = plot.StatButs(TableChoice,ChampionshipName)
st.pyplot(figure)