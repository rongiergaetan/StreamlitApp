#Visual Setting
ChampionshipColor = {"Bundesliga":"#006400","PremierLeague":"#6495ED","Liga":"#EEB422","SerieA":"#9400D3","Ligue1":"#DC143C"}



##########################################################################################################
#URL Setting
fbref = "https://fbref.com/fr/"
country = {"Bundesliga":"comps/20/Statistiques-Bundesliga","PremierLeague":"comps/9/Statistiques-Premier-League","Liga":"comps/12/Statistiques-La-Liga","SerieA":"comps/11/Statistiques-Serie-A",
"Ligue1":"comps/13/Statistiques-Ligue-1"}

#OutFunctionSetting
Dico_OutDatafBreb = {"which stat data table do you want ?":"Which stat data table do you want ?" ,"Classement":0, "BaseDataTeam":1, "AgainstBaseDataTeam":2, "GoalkeepingStat":3, "AgainstGoalkeepingStat":4, "AdvancedGoalkeepingStat":5, "AgainstAdvancedGoalkeepingStat":6, "DataShoots":7, "AgainstDataShoots":8, "PassStat":9, "AgainstPassStat":10, "PassStatType":11, "AgainstPassStatType":12, "OffensiveCreation":13, "AgainstOffensiveCreation":14, "DefensiveAction":15, "AgainstDefensiveAction":16, "Possession":17, "AgainstPossession":18}

#Glossaire
Dico_Def_Stat_Club = {"MP":"Match Played","W":"Wins","D":"Draws","L":"Losses","GF":"Goals for","GA":"Goal Against","GD":"Goal Difference","Pts":"Points","Poss":"Possession","Starts":"games started by a player","Min":"Minute played","90s":"90s minute played","Ast":"Assist",
"G-PK":"Non-Penalty Goal","PK":"Penalty kick made","PKatt":"Penalty kick attempted","CY":"Yellow cards","Red cards":"24","G/90":"Goal per 90s","A/90":"Assist per 90s","G+A/90":"Goal + Assist per 90s","G-PK/90":"Non-Penalty Goal per 90s","G+A-PK/90":"Non-Penalty Goal + Assist per 90s","xG":"Expected goal","npxG":"Non-Penalty expected goal","xA":"Expected assist","npxG+xA":"Non-Penalty expected goal + expected assist","xG/90":"Expected goal per 90s","xA/90":"Expected assist per 90s","xG+xA/90":"Expected goal + expected assist per 90s",
"npxG/90":"Non-Penalty goal per 90s","npxG+xA/90":"Non-Penalty goal + expected assist per 90","GA/90":"Goal aginst per 90s","SoTA":"Shoot on target against","saves":"goal saves","saves%":"Percentage goal saves","CS":"Clean sheets","CS%":"Percentage clean sheets","PKa":"Penalty kick allowed","PKsv":"Penalty kick saved","PKm":"Penalty Kick missed","PKsv%":"Percentage Penalty Kick saved","FKGA":"Free kick goal against","CKA":"Corner Kick Goals Against","CSC":"Own Goals Scored Against GoalKeeper","PSxG":"Post-shot Expected Goals (how likely the goalkeeper is to save the shot","PSxG/SoT":"Post-shot Expected Goals per Shot on target","PSxG+/-":"Post-shot Expected Goals minus Goals Allowed",
"PSxG+/-/90":"Post-shot Expected minus Goals allowed per 90mins","CMPLaunched":"Passes Longer than 35 metres completed","AttLaunched":"Passes Longer than 35 metres attempted","CMPLaunched%":"Percentage Passes Longer than 35 metres attempted","AttPass":"Passes attempted","ThrPass":"Throw attempted","Pass%":"Percentage passes launched (more than 35 metres","AvgLen":"Average length of passes, in yards","AttGoalKicks":"Goals Kick attempted","LaunchGaolKicks%":"Percentage of goals kick that were launched (more than 35 metres)","AvgLenGoalKicks":"Average length og goals kick","OppCrosses":"Opponent's attempted crosses into penalty area",
"StpCrosses":"crosses into penalty area successesfully stop by GoalKeeper","StpCrosses%":"Percentage crosses into penalty area successesfully stop by GoalKeeper","DefActOPA":"Defensive Action outside Penalty area","DefActOPA/90":"Defensice Action outside Penalty area per 90mins","AvgDistDefAct":"Average Distance from goal of all defensice action","Sh":"Shots","ShOT":"shots on target","ShOT%":"Percentage shot on target","Sh/90":"shots per 90mins","ShOT/90":"Shot on target per 90 mins","G/Sh":"Goals per shot","G/ShOT":"Goals per Shot on target","ShDist":"Average Distance; in yards, from goal of all shot taken","FK":"Free ick","PK":"Penalty Kick made","npxG/Sh":"Non-Penalty Expected Goals per shot",
"G-xG":"GOals minus expected Goals","np:G-xG":"Non-Penalty goals minus Non-Penalty Expected goalq","PCmp":"Passes Completed","PAtt":"Passes attempted","PCmp%":"Percentage passes completed","PTotDist":"Total distance, in yards, that completed passes have traveled in any direction","PPrgDist":"Total distance, in yards, that completed passes have traveled towards the opponent's goal","SPCmp":"Short Passes Completed","SPCmp%":"Percentage Short Passes Completed","SPAtt":"Short Passes attempted","MPCmp":"Medium Passes Completed (between 15 and 30 metres)","MPAtt":"Medium Passes attempted (between 15 and 30 metres)","MPCmp%":"Percentage Medium Passes Completed (between 15 and 30 metres)","LPCmp":"Long Passes Completed (more than 30 metres)","LPAtt":"Long Passes attempted (more than 30 metres)","LPCmp%":"Percentage Long Passes Completed","A":"Assist","A-xA":"Assist minus Expected assist",
"Ash":"Assisted shot (passes that lead to a shot)","P_1/3":"Passes completed that enter in the 1/3 of the pitch","Pass18YardBox":"Passes completed into the 18-yards box","CrsPA":"Completed crosses into the 18-yards box","PPrg":"Progressive Passes (Completed passes that move the towards the opponent's goal at least 10 metres)","PLive":"Live-ball passes","PDead":"Dead-ball passes","PFK":"Passes attempted from free kick","PbBD":"Completed passe send between back defenders into the open spase","Ppress":"Passes made while under pressure from opponent","P(<40m)":"Passes more than 40 metres","Crs":"Crosses","CK":"Corner kick","CIn":"Inswinging corner kick","COut":"Outswinging corner kick","CStraigt":"Straight corner kick",
"PGround":"Ground passes","PLow":"Passes that leave the ground but stay below shoulder-level","PHigh":"Passes that abow shoulder-level","BPLeft":"Passes attempted using left foot","BPRight":"Passes attempted using right foot","BPHead":"Passes attempted using head","throwIns":"throw_Ins taken","BPOther":"Passes attempted using other body parts","POff":"Passes offside","POut":"Passes Out of bounds","PInt":"Passes intercepted","PBlocks":"Passes Blocked by the opponent","SCA":"Shot creating action","SCA90":"Shot creating action by 90mins","SCAPassLive":"Completed passes that lead to a shot",
"SCAPassDead":"Completed Dead-ball passe that lead to a shot","SCASh":"shot that lead to another shot","SCAdrb":"Dribl that lead to a shot","SCAFoulsdrawn":"Fouls drawn that lead to a shot","SCADef":"defensive action that lead to a shot","GCA":"Goal creating action","GCA90":"Goal creating action per 90mins","GCAPassLive":"Live passes that lead to a goal","GCAPassDead":"Dead-ball passes that lead to a goal","GCADrib":"Dribble that lead to a goal","GCAFoulsdrawn":"Fouls drawn that lead to a goal","GCADef":"Defensiva action that lead to a goal","Tkl":"Number of player tackled","Tklsuccess":"Tackles in which the tackler's team won the ball possesion","TklDef3rd":"Tackles in the defensive 1/3",
"TklMid3rd":"Tackles in the middle 1/3","TKlAtt3rdkl":"Tackles in the attacking 1/3","DribTkl":"Numbers of dribbler tackled","Drib+Tkl":"Number of time dribbled past plus number of tackles","DribTkl%":"Percentage of dribblers tackled","DribPast":"Number of time Dribbled past","Press":"Number of time applying pressure to opposing player who is recieving","PressSucc":"Number of times the squad gained possesion within five second of applaying pressure","PressSucc%":"Percentage pressure success","PressDef3rd":"Number of time applying pressure to opposing player who is recieving in defensive 1/3","PressMid3rd":"Number of time applying pressure to opposing player who is recieving in middle 1/3","PressAtt3rd":"Number of time applying pressure to opposing player who is recieving in attacking 1/3","Blocks":"Number of time blocking the ball in stading in its path",
"BlockShoot":"Number of times blocking a shot","ShSv":"Number of times blocking a shot on target","BlockPass":"Number of times blocking a pass","Int":"Interception","Tkl+Int":"Tackles plus interception","Clr":"Clearances","ErrLSh":"Error leading to an opponent's shot","Tch":"Numbers of time players touch the ball","TchDefPen":"Numbers of time players touch the ball in defensive penalty area","TchDef3rd":"Numbers of time players touch the ball in defensive 1/3","TchMid3rd":"Numbers of time players touch the ball in middle 1/3","TchAtt3rd":"Numbers of time players touch the ball in attacking 1/3","TchAttPen":"Numbers of time players touch the ball in attacking penalty area","TchLive":"Live-ball touches (Not include stop phases","DribSucc":"Dribbled completed",
"DribAtt":"Dribbled attempted","DribSucc%":"Percentage dribbled completedm","PrDrib":"Numbers of players dribbled","DribMegs":"Number of time a player dribbled the ball through an opponent player's legs","Ca":"Number of time players carries the ball with their feet","CaTotDist":"Total distance, in XX, a player moved the ball while controling it with thei feet","ProgCaDist":"Total Progressive distance, in XX, a player moved the ball while controling it with their feet","ProgCa(>5m)":"Total progressive distance, in XX, a player moved the ball while controling it with their feet at least 5 yards","Car1/3":"Carries that ennter the 1/3 of the pitch closest the goal","Ca18Box":"Carries into the 18yards box area","Miss":"Numbers of time players miss to gain the control of the ball","LooseCaTkl":"Numbers of time plyaers losses control of the ball after being tackled","TarPass":"Numbers of time players was the target of an attempted pass","TarRec":"Numbers of time players successesfully received a pass","TarRec%":"Percentage successesfully received a pass","ProgRecSucc":"Numbers of time players successesfully received a progessive pass"}
	