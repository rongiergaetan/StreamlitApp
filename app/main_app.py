import streamlit as st
import pandas as pd 
import sys
import plot
import subprocess

st.title('Stat Tirs')



Championshipchoice = st.sidebar.selectbox("which Championship do you want ?",("Tirs_Bundesliga.csv","Tirs_PL.csv","Tirs_liga.csv","Tirs_SerieA.csv","Tirs_L1.csv") )


x = subprocess.run(['ls'])
print(x)

choice = "app/data/" + Championshipchoice
TableChoice = pd.read_csv("/data/Tirs_Bundesliga.csv")
ChampionshipName = choice.split("_")[1].split(".")[0]


figure = plot.StatButs(TableChoice,ChampionshipName)
st.pyplot(figure)
