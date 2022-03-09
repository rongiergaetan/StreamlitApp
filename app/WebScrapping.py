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
		for row in range(0,17):
			TeamName = Team[0].text
			Data=[]
			for col in range(0,12):
				value = DataClassement[col].text.split(",")
				if value[0] == '':
					value = ["0"]
				Data.append(float(".".join(value)))
			Data = [TeamName] + Data
			Data = [row+1] + Data
			Classement[row+1] = Data
			del Team[0:3]
			del DataClassement[0:15]
		#RemoveAwayHome
		for row in range(0,17):
			del DataClassement[0:26]
			del Team[0]
		#DataTeamBAse
		Team = pageSoup.find_all("th",{"class":"left"})
		centre = pageSoup.find_all("td",{"class":"center"})
		for row in range(0,17):
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
		#DataTeamBAse
		for row in range(0,17):
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
		for row in range(0,17):
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
				Data.append(float(".".join(value)))
			del Data[10:13]
			del Data[2]
			AgainstGoalkeepingStat["Against " + Team[row].text] = Data	
			del DataClassement[0:20]
		#AdvancedgoalkeepingStat 5
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
			Data=[]
			for col in range(0,24):
				Data.append(float(float(DataClassement[col].text)))
			del Data[0:2]
			AgainstPassStat["Against " + Team[row].text] = Data	
			del DataClassement[0:24]
		#SquadPassType 11
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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
		for row in range(0,17):
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

	#CLassement
	df_Classement = pd.DataFrame.from_dict(Classement, orient='index', columns=['Classement', 'Equipe', 'MJ', 'V', 'N', 'D', 'BM', 'BE', 'DB', 'Pts', 'xG', 'xGA', 'xGD', 'xGD/90'])
	Pts_column = df_Classement.pop('Pts')
	df_Classement.insert(6, 'Pts', Pts_column)
	#BaseDataTeam
	df_AgainstBaseDataTeam = pd.DataFrame.from_dict(AgainstBaseDataTeam, orient='index', columns=["Âge","Poss","PlayerUsed","MJ","Titulaire","Min","90","Buts","PD","B-PénM","PénM","PénT","CJ","CR","Buts/90","PD/90","B+PD/90","B-PénM/90","B+PD-PénM/90","xG","npxG","xA","npxG+xA","xG/90","xA/90","xG+xA/90","npxG/90","npxG+xA/90"])
	df_BaseDataTeam = pd.DataFrame.from_dict(BaseDataTeam, orient='index', columns=["Âge","Poss","PlayerUsed","MJ","Titulaire","Min","90","Buts","PD","B-PénM","PénM","PénT","CJ","CR","Buts/90","PD/90","B+PD/90","B-PénM/90","B+PD-PénM/90","xG","npxG","xA","npxG+xA","xG/90","xA/90","xG+xA/90","npxG/90","npxG+xA/90"])
	#GoalKeeperStat
	df_AgainstGoalkeepingStat = pd.DataFrame.from_dict(AgainstGoalkeepingStat, orient='index', columns=["PlayerUsed","MJ","Min","90","BE","BE90","TCC","saves","saves%","CleanSheets","CleanSheets%","PKAtt","PKallowed","PKsv","PKm","PKsave%"])
	df_GoalkeepingStat = pd.DataFrame.from_dict(GoalkeepingStat, orient='index', columns=["PlayerUsed","MJ","Min","90","BE","BE90","TCC","saves","saves%","CleanSheets","CleanSheets%","PKAtt","PKallowed","PKsv","PKm","PKsave%"])
	#AdvancedGoalkeepingStat
	df_AdvancedGoalkeepingStat = pd.DataFrame.from_dict(AdvancedGoalkeepingStat, orient='index', columns=["GA","PGAA","FKGA","CoGA","CSC","PSxG","PSxG/SoT","PSxG+/-","PSxG+/-/90","CompletedLaunched","AttLaunched","CompletedLaunched%","AttPass","LancPass","LaunchPass%","LongMoyPass","AttGoalKicks","LaunchGaolKicks%","LongMoyGoalKicks","OppAttCrosses","StopCrosses","StopCrosses%","defensivActionOutsidePenaltyArea","defensivActionOutsidePenaltyArea/90","DistMoy"])
	df_AgainstAdvancedGoalkeepingStat = pd.DataFrame.from_dict(AgainstAdvancedGoalkeepingStat, orient='index', columns=["GA","PGAA","FKGA","CoGA","CSC","PSxG","PSxG/SoT","PSxG+/-","PSxG+/-/90","CompletedLaunched","AttLaunched","CompletedLaunched%","AttPass","LancPass","LaunchPass%","LongMoyPass","AttGoalKicks","LaunchGaolKicks%","LongMoyGoalKicks","OppAttCrosses","StopCrosses","StopCrosses%","defensivActionOutsidePenaltyArea","defensivActionOutsidePenaltyArea/90","DistMoy"])
	#DataShoot
	df_DataShoots = pd.DataFrame.from_dict(DataShoots, orient='index', columns=["Goal","Sh","ShOT","ShOT%","Sh/90","ShOT/90","G/Sh","G/ShOT","ShAverageDist","FK","PKG","PKatt","xG","npxG","npxG/Sh","G-xG","np:G-xG"])
	df_AgainstDataShoots = pd.DataFrame.from_dict(AgainstDataShoots, orient='index', columns=["Goal","Sh","ShOT","ShOT%","Sh/90","ShOT/90","G/Sh","G/ShOT","ShAverageDist","FK","PKG","PKatt","xG","npxG","npxG/Sh","G-xG","np:G-xG"])
	#PassStat
	df_PassStat = pd.DataFrame.from_dict(PassStat, orient='index', columns=["PassCompleted","PassAttempted","PassCompleted%","PassTotDist","PassprogressiveDist","ShortPassCompleted","ShortAttempt","ShortPassCompleted%","MediumPassCompleted","MediumPassAttempt","MediumPassCompleted%","LongPassCompleted","LongPassAttempt","LongPassCompleted%","Assists","xA","A-xA","PostShoot","Last_1/3_Pass","Pass18YardBox","CntSR","PAssProg"])
	df_AgainstPassStat = pd.DataFrame.from_dict(AgainstPassStat, orient='index', columns=["PassCompleted","PassAttempted","PassCompleted%","PassTotDist","PassprogressiveDist","ShortPassCompleted","ShortAttempt","ShortPassCompleted%","MediumPassCompleted","MediumPassAttempt","MediumPassCompleted%","LongPassCompleted","LongPassAttempt","LongPassCompleted%","Assists","xA","A-xA","PostShoot","Last_1/3_Pass","Pass18YardBox","CntSR","PAssProg"])
	#SquadPassType
	df_PassStatType = pd.DataFrame.from_dict(PassStatType, orient='index', columns=["PassAttempt","Live","Dead","FreeKick","BetweenBackDefenders","Press","LongPass(<40m)","Crosses","CornerKick","CornerIn","CornerOut","CornerStraigt","Ground","Low","High","BodyPartLeft","BodyPartRight","BodyPartHead","throw_ins","Other","PassCompleted","Off","Out","Intercepted","Blocks"])
	df_AgainstPassStatType = pd.DataFrame.from_dict(AgainstPassStatType, orient='index', columns=["PassAttempt","Live","Dead","FreeKick","BetweenBackDefenders","Press","LongPass(<40m)","Crosses","CornerKick","CornerIn","CornerOut","CornerStraigt","Ground","Low","High","BodyPartLeft","BodyPartRight","BodyPartHead","throw_ins","Other","PassCompleted","Off","Out","Intercepted","Blocks"])
	#SQuadGoalAndSHotCreation
	df_OffensiveCreation = pd.DataFrame.from_dict(OffensiveCreation, orient='index', columns=["ShotCreatingAction(SCA)","SCA90","SCAPassLive","SCAPassDead","SCADrib","SCASh","SCAFoulsdranw","SCADef","GoalCreatingAction(GCA)","GCA90","GCAPassLive","GCAPassDead","GCADrib","GCASh","GCAFoulsdrawn","GCADef"])
	df_AgainstOffensiveCreation = pd.DataFrame.from_dict(AgainstOffensiveCreation, orient='index', columns=["ShotCreatingAction(SCA)","SCA90","SCAPassLive","SCAPassDead","SCADrib","SCASh","SCAFoulsdranw","SCADef","GoalCreatingAction(GCA)","GCA90","GCAPassLive","GCAPassDead","GCADrib","GCASh","GCAFoulsdrawn","GCADef"])
	#SquandDefensiveAction
	df_DefensiveAction = pd.DataFrame.from_dict(DefensiveAction, orient='index', columns=["Takle(Tkl)","Tklsuccess","TklDef 3rd","TklMid 3rd","TKlAtt 3rd","TklVSdribbles","DribbledPast+Tkl","Tkl% VSdribbles","DribblesPast","NumberPressure","PressSucc","%PressSucc","PressDef 3rd","PressMid 3rd","PressAtt 3rd","BlocksBall","BlockShoot","ShSv","BlockPass","Interception(Int)","Tkl+Int","Clearances","ErrLeadShoot"])
	df_AgainstDefensiveAction = pd.DataFrame.from_dict(AgainstDefensiveAction, orient='index', columns=["Takle(Tkl)","Tklsuccess","TklDef 3rd","TklMid 3rd","TKlAtt 3rd","TklVSdribbles","DribbledPast+Tkl","Tkl% VSdribbles","DribblesPast","NumberPressure","PressSucc","%PressSucc","PressDef 3rd","PressMid 3rd","PressAtt 3rd","BlocksBall","BlockShoot","ShSv","BlockPass","Interception(Int)","Tkl+Int","Clearances","ErrLeadShoot"])
	#SquadPossesion
	df_Possession = pd.DataFrame.from_dict(Possession, orient='index', columns=["Touches(Tch)","TchDef Pen","TchDef 3rd","TchMid 3rd","TchAtt 3rd","TchAtt Pen","TchLive","DribblesSucc","DribblesAtt","DribblesSucc%","PlayerDribbled","DribblesMegs","Carries","CarriesTotalDist","ProgressiveCarriesDist","ProgCarries(>5m)","Carries1/3","Carries 18_yard box","Miss","LooseCarriesByTkl","TargetByPass","ReceiveSuccess","ReceiveSuccess%","ProgressiveReceiveSuccess"])
	df_AgainstPossession = pd.DataFrame.from_dict(AgainstPossession, orient='index', columns=["Touches(Tch)","TchDef Pen","TchDef 3rd","TchMid 3rd","TchAtt 3rd","TchAtt Pen","TchLive","DribblesSucc","DribblesAtt","DribblesSucc%","PlayerDribbled","DribblesMegs","Carries","CarriesTotalDist","ProgressiveCarriesDist","ProgCarries(>5m)","Carries1/3","Carries 18_yard box","Miss","LooseCarriesByTkl","TargetByPass","ReceiveSuccess","ReceiveSuccess%","ProgressiveReceiveSuccess"])


	return df_Classement, df_BaseDataTeam, df_AgainstBaseDataTeam, df_GoalkeepingStat, df_AgainstGoalkeepingStat, df_AdvancedGoalkeepingStat, df_AgainstAdvancedGoalkeepingStat, df_DataShoots, df_AgainstDataShoots, df_PassStat, df_AgainstPassStat, df_PassStatType, df_AgainstPassStatType, df_OffensiveCreation, df_AgainstOffensiveCreation, df_DefensiveAction, df_AgainstDefensiveAction, df_Possession, df_AgainstPossession


a  = DatafBref(MakeURL(st.fbref,st.country,"Ligue1"),"Ligue1")