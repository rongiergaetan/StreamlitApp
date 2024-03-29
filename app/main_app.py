import streamlit as stl
import pandas as pd 
import sys
import plot
import subprocess
import WebScrapping as ws
import setting as st

###############################################################################
#Choix du championnat Etudier
Championshipchoice = stl.sidebar.selectbox("which Championship do you want ?",("Ligue1","Liga","Bundesliga","PremierLeague","SerieA") )
ChampionshipName = Championshipchoice

#choix du tableau statistique de comparaison
StatDataTable = stl.sidebar.selectbox("Statistic Data Table Selectbox",("which stat data table do you want ?", "BaseDataTeam", "AgainstBaseDataTeam", "GoalkeepingStat", "AgainstGoalkeepingStat", "AdvancedGoalkeepingStat", "AgainstAdvancedGoalkeepingStat", "DataShoots", "AgainstDataShoots", "PassStat", "AgainstPassStat", "PassStatType", "AgainstPassStatType", "OffensiveCreation", "AgainstOffensiveCreation", "DefensiveAction", "AgainstDefensiveAction", "Possession","AgainstPossession") )

###############################################################################
#Classement
DataFbref = ws.DatafBref(ws.MakeURL(st.fbref,st.country,ChampionshipName),ChampionshipName)

stl.title("Classement")
stl.table(DataFbref[0])
stl.write("source: fbref")


 #tableau statistique
stl.title("Statistic")

if StatDataTable == "which stat data table do you want ?":
	stl.write("which stat data table do you want ?")
	stl.write(" choice in the sidedebar with the second selectbox")
else:
	stl.write(StatDataTable)
	df_stat_team = st.Dico_OutDatafBreb[StatDataTable]
	stl.table(DataFbref[df_stat_team])
	stl.write("source: fbref")

	#Barplot Stat Team
	List = ["Which Team do you want to compare ?"]
	for i in DataFbref[df_stat_team].index:
		List.append(i)
	Team_choice_1 = stl.sidebar.selectbox("Choice first team to compare",(List))
	Team_choice_2 = stl.sidebar.selectbox("Choice second team to compare",(List))

	if Team_choice_2 == "Which Team do you want to compare ?":
		stl.write("You can choice two team to compare in the sidebar")
	else:
		stl.write("Barplot")
		Barplot = plot.BarplotTeamStat(DataFbref[df_stat_team],Team_choice_1,Team_choice_2)
		for i in Barplot:
			stl.pyplot(i)

TermToDef = stl.sidebar.text_input("statistical glossary of terms", value="datatable variable that you want defining")
if TermToDef == "datatable variable that you want defining":
	pass
elif	 TermToDef in st.Dico_Def_Stat_Club:
	stl.sidebar.write(TermToDef + ": " + st.Dico_Def_Stat_Club[TermToDef])
else:
	stl.sidebar.write(TermToDef + ": variable you want defining doesn't exist in our glossary. Make sure you use the same orthograph than in the datatable (take attention to minuscule and majuscule)")
