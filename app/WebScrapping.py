from bs4 import BeautifulSoup
import pandas as pd
import requests
import setting as st

def MakeURL(Start_URL,End_URL,dico_Key):
	pageTree = requests.get(Start_URL + End_URL[dico_Key])
	pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
	return pageSoup



def DatafBref(pageSoup,NB_Team):
	DataClassement = pageSoup.find_all("td",{"class":"right"})  #14 colonne et 20row, 17Bundes
	Team = pageSoup.find_all("td",{"class":"left"})
	Classement = {}
	if NB_Team == "Bundesliga":
		for row in range(0,17):
			TeamName = Team[0].text
			Data=[]
			for col in range(0,12):
				Data.append(DataClassement[col].text)
			Data = [TeamName] + Data
			Data = [row+1] + Data
			Classement[row+1]=Data
			del Team[0:3]
			del DataClassement[0:15]
	else:
		for row in range(0,20):
			TeamName = Team[0].text
			Data=[]
			for col in range(0,12):
				Data.append(DataClassement[col].text)
			Data = [TeamName] + Data
			Data = [row+1] + Data
			Classement[row+1]=Data
			del Team[0:3]
			del DataClassement[0:15]

	df_Classement = pd.DataFrame.from_dict(Classement, orient='index', columns=['Classement', 'Equipe', 'MJ', 'V', 'N', 'D', 'BM', 'BE', 'DB', 'Pts', 'xG', 'xGA', 'xGD', 'xGD/90'])
	Pts_column = df_Classement.pop('Pts')
	df_Classement.insert(6, 'Pts', Pts_column)
	return df_Classement