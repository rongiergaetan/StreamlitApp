import streamlit as stl
import pandas as pd 
import sys
import plot
import subprocess
import WebScrapping as ws
import setting as st

###############################################################################
#Choix du championnat Etudier
Championshipchoice = stl.sidebar.selectbox("which Championship do you want ?",("Tirs_liga.csv","Tirs_Ligue1.csv","Tirs_Bundesliga.csv","Tirs_PremierLeague.csv","Tirs_SerieA.csv") )
ChampionshipName = Championshipchoice.split("_")[1].split(".")[0]

#choix du tableau statistique de comparaison
StatDataTable = stl.sidebar.selectbox("which stat data table do you want ?",("stat table list", "BaseDataTeam", "AgainstBaseDataTeam", "GoalkeepingStat", "AgainstGoalkeepingStat", "AdvancedGoalkeepingStat", "AgainstAdvancedGoalkeepingStat", "DataShoots", "AgainstDataShoots", "PassStat", "AgainstPassStat", "PassStatType", "AgainstPassStatType", "OffensiveCreation", "AgainstOffensiveCreation", "DefensiveAction", "AgainstDefensiveAction", "Possession","AgainstPossession") )

###############################################################################
#Classement
DataFbref = ws.DatafBref(ws.MakeURL(st.fbref,st.country,ChampionshipName),ChampionshipName)

stl.title("Classement")
stl.dataframe(DataFbref[0],width=1000,height=1000)
stl.write("source: fbref")

stl.write("\t\t")

 #tableau statistique
stl.title(StatDataTable)
stl.dataframe(DataFbref[st.Dico_OutDatafBreb[StatDataTable]],width=1000,height=1000)
stl.write("source: fbref")