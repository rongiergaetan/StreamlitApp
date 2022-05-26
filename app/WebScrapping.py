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
	BaseDataTeam = {}
	AgainstBaseDataTeam = {}
	GoalkeepingStat = {}
	AgainstGoalkeepingStat = {}
	AdvancedGoalkeepingStat = {}
	AgainstAdvancedGoalkeepingStat = {}
	DataShoots = {}
	AgainstDataShoots = {}
	PassStat = {}
	AgainstPassStat = {}
	PassStatType = {}
	AgainstPassStatType = {}
	OffensiveCreation = {}
	AgainstOffensiveCreation = {}
	DefensiveAction = {}
	AgainstDefensiveAction = {}
	Possession = {}
	AgainstPossession = {}



	if NB_Team == "Bundesliga":
		for row in range(0,18):
			TeamName = Team[0].text
			Data=[]
			for col in range(0,12):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			Data = [TeamName] + Data
			Data = [row+1] + Data
			del Data[10:]
			Classement[row+1] = Data
			del Team[0:3]
			del DataClassement[0:15]
		#RemoveAwayHome
		for row in range(0,18):
			del DataClassement[0:26]
			del Team[0]
		#DataTeamBAse
		Team = pageSoup.find_all("th",{"class":"left"})
		centre = pageSoup.find_all("td",{"class":"center"})
		for row in range(0,18):
			Data = []
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			Data = [centre[1].text] + Data
			Data = [centre[0].text] + Data
			BaseDataTeam[Team[row].text] = Data	
			del DataClassement[0:26]
			del centre[0:2]
		#DataTeamBAseAgainst
		for row in range(0,18):
			Data = []
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			Data = [centre[1].text] + Data
			Data = [centre[0].text] + Data
			AgainstBaseDataTeam["Against " + Team[row].text] = Data		
			del DataClassement[0:26]
			del centre[0:2]
			del centre[0:2]
		#goalkeepingStat 3
		for row in range(0,18):
			Data=[]
			for col in range(0,20):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[10:13]
			del Data[2]
			GoalkeepingStat[Team[row].text] = Data	
			del DataClassement[0:20]
		#AgaintGoalkeepingStat 4
		for row in range(0,18):
			Data=[]
			for col in range(0,20):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[10:13]
			del Data[2]
			AgainstGoalkeepingStat["Against " + Team[row].text] = Data	
			del DataClassement[0:20]
		#AdvancedgoalkeepingStat 5
		for row in range(0,18):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AdvancedGoalkeepingStat[Team[row].text] = Data	
			del DataClassement[0:27]
		#AgaintAdvancedGoalkeepingStat 6
		for row in range(0,18):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstAdvancedGoalkeepingStat["Against " + Team[row].text] = Data	
			del DataClassement[0:27]
		#ShootStat 7
		for row in range(0,18):
			Data=[]
			for col in range(0,19):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			DataShoots[Team[row].text] = Data	
			del DataClassement[0:19]
		#AgaintShootStat 8
		for row in range(0,18):
			Data=[]
			for col in range(0,19):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstDataShoots["Against " + Team[row].text] = Data	
			del DataClassement[0:19]
		#PassStat 9
		for row in range(0,18):
			Data=[]
			for col in range(0,24):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			PassStat[Team[row].text] = Data	
			del DataClassement[0:24]
		#AgaintPassStat 10
		for row in range(0,18):
			Data=[]
			for col in range(0,24):
				Data.append(float(float(DataClassement[col].text)))
			del Data[0:2]
			AgainstPassStat["Against " + Team[row].text] = Data	
			del DataClassement[0:24]
		#SquadPassType 11
		for row in range(0,18):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			PassStatType[Team[row].text] = Data	
			del DataClassement[0:27]
		#AgaintSquadPassType 12
		for row in range(0,18):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstPassStatType["Against " + Team[row].text] = Data	
			del DataClassement[0:27]
		#SQuadGoalAndSHotCreation 13
		for row in range(0,18):
			Data=[]
			for col in range(0,18):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			OffensiveCreation[Team[row].text] = Data	
			del DataClassement[0:18]
		#SQuadGoalAndSHotCreation 14
		for row in range(0,18):
			Data=[]
			for col in range(0,18):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstOffensiveCreation["Against " + Team[row].text] = Data	
			del DataClassement[0:18]
		#SquadDefensiveAction 15
		for row in range(0,18):
			Data=[]
			for col in range(0,25):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			DefensiveAction[Team[row].text] = Data	
			del DataClassement[0:25]
		#AgainstSquadDefensiveAction 16
		for row in range(0,18):
			Data=[]
			for col in range(0,25):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstDefensiveAction[Team[row].text] = Data	
			del DataClassement[0:25]
		#SquadPossesion17
		for row in range(0,18):
			Data=[]
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			Possession[Team[row].text] = Data	
			del DataClassement[0:26]
		#AgainstSquadpossession 18
		for row in range(0,18):
			Data=[]
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstPossession[Team[row].text] = Data	
			del DataClassement[0:26]




	else:
		#Classement 0
		for row in range(0,20):
			TeamName = Team[0].text
			Data=[]
			for col in range(0,12):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			Data = [TeamName] + Data
			Data = [row+1] + Data
			del Data[10:]
			Classement[row+1]=Data
			del Team[0:3]
			del DataClassement[0:15]

		#RemoveAwayHome
		for row in range(0,20):
			del DataClassement[0:26]
			del Team[0]
		#DataTeamBAse 1
		Team = pageSoup.find_all("th",{"class":"left"})
		centre = pageSoup.find_all("td",{"class":"center"})
		for row in range(0,20):
			Data = []
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			Data = [centre[1].text] + Data
			Data = [centre[0].text] + Data
			BaseDataTeam[Team[row].text] = Data	
			del DataClassement[0:26]
			del centre[0:2]
		#DataTeamBAse 2
		for row in range(0,20):
			Data = []
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			Data = [centre[1].text] + Data
			Data = [centre[0].text] + Data
			AgainstBaseDataTeam["Against " + Team[row].text] = Data		
			del DataClassement[0:26]
			del centre[0:2]
		#goalkeepingStat 3
		for row in range(0,20):
			Data=[]
			for col in range(0,20):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[10:13]
			del Data[2]
			GoalkeepingStat[Team[row].text] = Data	
			del DataClassement[0:20]
		#AgaintGoalkeepingStat 4
		for row in range(0,20):
			Data=[]
			for col in range(0,20):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[10:13]
			del Data[2]
			AgainstGoalkeepingStat["Against " + Team[row].text] = Data	
			del DataClassement[0:20]
		#AdvancedgoalkeepingStat 5
		for row in range(0,20):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AdvancedGoalkeepingStat[Team[row].text] = Data	
			del DataClassement[0:27]
		#AgaintAdvancedGoalkeepingStat 6
		for row in range(0,20):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstAdvancedGoalkeepingStat["Against " + Team[row].text] = Data	
			del DataClassement[0:27]
		#ShootStat 7
		for row in range(0,20):
			Data=[]
			for col in range(0,19):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			DataShoots[Team[row].text] = Data	
			del DataClassement[0:19]
		#AgaintShootStat 8
		for row in range(0,20):
			Data=[]
			for col in range(0,19):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstDataShoots["Against " + Team[row].text] = Data	
			del DataClassement[0:19]
		#PassStat 9
		for row in range(0,20):
			Data=[]
			for col in range(0,24):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			PassStat[Team[row].text] = Data	
			del DataClassement[0:24]
		#AgaintPassStat 10
		for row in range(0,20):
			Data=[]
			for col in range(0,24):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstPassStat["Against " + Team[row].text] = Data	
			del DataClassement[0:24]
		#SquadPassType 11
		for row in range(0,20):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			PassStatType[Team[row].text] = Data	
			del DataClassement[0:27]
		#AgaintSquadPassType 12
		for row in range(0,20):
			Data=[]
			for col in range(0,27):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstPassStatType["Against " + Team[row].text] = Data	
			del DataClassement[0:27]
		#SQuadGoalAndSHotCreation 13
		for row in range(0,20):
			Data=[]
			for col in range(0,18):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			OffensiveCreation[Team[row].text] = Data	
			del DataClassement[0:18]
		#SQuadGoalAndSHotCreation 14
		for row in range(0,20):
			Data=[]
			for col in range(0,18):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstOffensiveCreation["Against " + Team[row].text] = Data	
			del DataClassement[0:18]
		#SquadDefensiveAction 15
		for row in range(0,20):
			Data=[]
			for col in range(0,25):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			DefensiveAction[Team[row].text] = Data	
			del DataClassement[0:25]
		#AgainstSquadDefensiveAction 16
		for row in range(0,20):
			Data=[]
			for col in range(0,25):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstDefensiveAction[Team[row].text] = Data	
			del DataClassement[0:25]
		#SquadPossesion17
		for row in range(0,20):
			Data=[]
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			Possession[Team[row].text] = Data	
			del DataClassement[0:26]
		#AgainstSquadpossession 18
		for row in range(0,20):
			Data=[]
			for col in range(0,26):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			del Data[0:2]
			AgainstPossession[Team[row].text] = Data	
			del DataClassement[0:26]

	#CLassement'Classement', 'Equipe', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'
	#df_Classement = pd.DataFrame.from_dict(Classement, orient='index', columns=['Classement', 'Equipe', 'MJ', 'V', 'N', 'D', 'BM', 'BE', 'DB', 'Pts', 'xG', 'xGA', 'xGD', 'xGD/90'])
	df_Classement = pd.DataFrame.from_dict(Classement, orient='index', columns=['Classement', 'Equipe', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'])
	Pts_column = df_Classement.pop('Pts')
	df_Classement.insert(6, 'Pts', Pts_column)
	columns = list(df_Classement.columns)
	#convert value string to float
	for i  in range(len(columns)):
		if i+2 <= len(columns)-1:
			df_Classement[columns[i+2]] = pd.to_numeric(df_Classement[columns[i+2]],downcast="integer")
	#BaseDataTeam
	df_AgainstBaseDataTeam = pd.DataFrame.from_dict(AgainstBaseDataTeam, orient='index', columns=["Âge","Poss","PlayerUsed","MP","Starts","Min","90s","Goal","Ast","G-PK","PK","PKatt","CY","CR","G/90","A/90","G+A/90","G-PK/90","G+A-PK/90","xG","npxG","xA","npxG+xA","xG/90","xA/90","xG+xA/90","npxG/90","npxG+xA/90"])
	df_BaseDataTeam = pd.DataFrame.from_dict(BaseDataTeam, orient='index', columns=["Âge","Poss","PlayerUsed","MP","Starts","Min","90s","Goal","Ast","G-PK","PK","PKatt","CY","CR","G/90","A/90","G+A/90","G-PK/90","G+A-PK/90","xG","npxG","xA","npxG+xA","xG/90","xA/90","xG+xA/90","npxG/90","npxG+xA/90"])
	#GoalKeeperStat
	df_AgainstGoalkeepingStat = pd.DataFrame.from_dict(AgainstGoalkeepingStat, orient='index', columns=["PlayerUsed","MP","Min","90s","GA","GA/90","SoTA","saves","saves%","CS","CS%","PKAtt","PKa","PKsv","PKm","PKsv%"])
	df_GoalkeepingStat = pd.DataFrame.from_dict(GoalkeepingStat, orient='index', columns=["PlayerUsed","MP","Min","90s","GA","GA/90","SoTA","saves","saves%","CS","CS%","PKAtt","PKa","PKsv","PKm","PKsv%"])
	#AdvancedGoalkeepingStat
	df_AdvancedGoalkeepingStat = pd.DataFrame.from_dict(AdvancedGoalkeepingStat, orient='index', columns=["GA","PKa","FKGA","CKA","CSC","PSxG","PSxG/SoT","PSxG+/-","PSxG+/-/90","CMPLaunched","AttLaunched","CMPLaunched%","AttPass","ThrPass","Pass%","AvgLen","AttGoalKicks","LaunchGaolKicks%","AvgLenGoalKicks","OppCrosses","StpCrosses","StpCrosses%","DefActOPA","DefActOPA/90","AvgDist"])
	df_AgainstAdvancedGoalkeepingStat = pd.DataFrame.from_dict(AgainstAdvancedGoalkeepingStat, orient='index', columns=["GA","PKa","FKGA","CKA","CSC","PSxG","PSxG/SoT","PSxG+/-","PSxG+/-/90","CMPLaunched","AttLaunched","CMPLaunched%","AttPass","ThrPass","Pass%","AvgLen","AttGoalKicks","LaunchGaolKicks%","AvgLenGoalKicks","OppCrosses","StpCrosses","StpCrosses%","DefActOPA","DefActOPA/90","AvgDist"])
	#DataShoot
	df_DataShoots = pd.DataFrame.from_dict(DataShoots, orient='index', columns=["Goals","Sh","ShOT","ShOT%","Sh/90","ShOT/90","G/Sh","G/ShOT","ShDist","FK","PK","PKatt","xG","npxG","npxG/Sh","G-xG","np:G-xG"])
	df_AgainstDataShoots = pd.DataFrame.from_dict(AgainstDataShoots, orient='index', columns=["Goals","Sh","ShOT","ShOT%","Sh/90","ShOT/90","G/Sh","G/ShOT","ShDist","FK","PK","PKatt","xG","npxG","npxG/Sh","G-xG","np:G-xG"])
	#PassStat
	df_PassStat = pd.DataFrame.from_dict(PassStat, orient='index', columns=["PCmp","PAtt","PCmp%","PTotDist","PPrgDist","SPCmp","SPAtt","SPCmp%","MPCmp","MPAtt","MPCmp%","LPCmp","LPAtt","LPCmp%","A","xA","A-xA","Ash","P_1/3","Pass18YardBox","CrsPA","PPrg"])
	df_AgainstPassStat = pd.DataFrame.from_dict(AgainstPassStat, orient='index', columns=["PCmp","PAtt","PCmp%","PTotDist","PPrgDist","SPCmp","SPAtt","SPCmp%","MPCmp","MPAtt","MPCmp%","LPCmp","LPAtt","LPCmp%","A","xA","A-xA","Ash","P_1/3","Pass18YardBox","CrsPA","PPrg"])
	#SquadPassType
	df_PassStatType = pd.DataFrame.from_dict(PassStatType, orient='index', columns=["PAtt","PLive","PDead","PFK","PbBD","Ppress","P(<40m)","Crs","CK","CIn","COut","CStraigt","PGround","PLow","PHigh","BPLeft","BPRight","BPHead","throwIns","BPOther","PCmp","POff","POut","PInt","PBlocks"])
	df_AgainstPassStatType = pd.DataFrame.from_dict(AgainstPassStatType, orient='index', columns=["PAtt","PLive","PDead","PFK","PbBD","Ppress","P(<40m)","Crs","CK","CIn","COut","CStraigt","PGround","PLow","PHigh","BPLeft","BPRight","BPHead","throwIns","BPOther","PCmp","POff","POut","PInt","PBlocks"])
	#SQuadGoalAndSHotCreation
	df_OffensiveCreation = pd.DataFrame.from_dict(OffensiveCreation, orient='index', columns=["SCA","SCA90","SCAPassLive","SCAPassDead","SCADrib","SCASh","SCAFoulsdrawn","SCADef","GCA","GCA90","GCAPassLive","GCAPassDead","GCADrib","GCASh","GCAFoulsdrawn","GCADef"])
	df_AgainstOffensiveCreation = pd.DataFrame.from_dict(AgainstOffensiveCreation, orient='index', columns=["SCA","SCA90","SCAPassLive","SCAPassDead","SCADrib","SCASh","SCAFoulsdrawn","SCADef","GCA","GCA90","GCAPassLive","GCAPassDead","GCADrib","GCASh","GCAFoulsdrawn","GCADef"])
	#SquandDefensiveAction
	df_DefensiveAction = pd.DataFrame.from_dict(DefensiveAction, orient='index', columns=["Tkl","Tklsuccess","TklDef3rd","TklMid3rd","TKlAtt3rd","DribTkl","Drib+Tkl","DribTkl%","DribPast","Press","PressSucc","PressSucc%","PressDef3rd","PressMid3rd","PressAtt3rd","Blocks","BlockShoot","ShSv","BlockPass","Int","Tkl+Int","Clr","ErrLSh"])
	df_AgainstDefensiveAction = pd.DataFrame.from_dict(AgainstDefensiveAction, orient='index', columns=["Tkl","Tklsuccess","TklDef3rd","TklMid3rd","TKlAtt3rd","DribTkl","Drib+Tkl","DribTkl%","DribPast","Press","PressSucc","PressSucc%","PressDef3rd","PressMid3rd","PressAtt3rd","Blocks","BlockShoot","ShSv","BlockPass","Int","Tkl+Int","Clr","ErrLSh"])
	#SquadPossesion
	df_Possession = pd.DataFrame.from_dict(Possession, orient='index', columns=["Tch","TchDefPen","TchDef3rd","TchMid3rd","TchAtt3rd","TchAttPen","TchLive","DribSucc","DribAtt","DribSucc%","PrDrib","DribMegs","Ca","CaTotDist","ProgCaDist","ProgCa(>5m)","Car1/3","Ca18Box","Miss","LooseCaTkl","TarPass","TarRec","TarRec%","ProgRecSucc"])
	df_AgainstPossession = pd.DataFrame.from_dict(AgainstPossession, orient='index', columns=["Tch","TchDefPen","TchDef3rd","TchMid3rd","TchAtt3rd","TchAttPen","TchLive","DribSucc","DribAtt","DribSucc%","PrDrib","DribMegs","Ca","CaTotDist","ProgCaDist","ProgCa(>5m)","Car1/3","Ca18Box","Miss","LooseCaTkl","TarPass","TarRec","TarRec%","ProgRecSucc"])

	return df_Classement, df_BaseDataTeam, df_AgainstBaseDataTeam, df_GoalkeepingStat, df_AgainstGoalkeepingStat, df_AdvancedGoalkeepingStat, df_AgainstAdvancedGoalkeepingStat, df_DataShoots, df_AgainstDataShoots, df_PassStat, df_AgainstPassStat, df_PassStatType, df_AgainstPassStatType, df_OffensiveCreation, df_AgainstOffensiveCreation, df_DefensiveAction, df_AgainstDefensiveAction, df_Possession, df_AgainstPossession


a  = DatafBref(MakeURL(st.fbref,st.country,"Ligue1"),"Ligue1")