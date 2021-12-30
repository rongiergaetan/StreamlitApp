import streamlit as stl
import pandas as pd 
import sys
import plot
import subprocess
import WebScrapping as ws
import setting as st

stl.title('Stat Tirs')


###############################################################################
#Choix du championnat Etudier
Championshipchoice = stl.sidebar.selectbox("which Championship do you want ?",("Tirs_liga.csv","Tirs_Ligue1.csv","Tirs_Bundesliga.csv","Tirs_PremierLeague.csv","Tirs_SerieA.csv") )
x = subprocess.run(['ls'])
choice = "app/data/" + Championshipchoice
TableChoice = pd.read_csv(choice)
ChampionshipName = choice.split("_")[1].split(".")[0]

###############################################################################
#FirstPLot
figure = plot.StatButs(TableChoice,ChampionshipName)
stl.pyplot(figure)

###############################################################################
#Classement
stl.title('Classement')
TClassement = ws.DatafBref(ws.MakeURL(st.fbref,st.country,ChampionshipName),ChampionshipName)
stl.dataframe(TClassement,width=1000,height=1000)
stl.write("source: fbref")