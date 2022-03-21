import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import setting as st
import numpy as np


def StatButs(TableChoice,ChampionshipName):
	fig = plt.figure(figsize=(12,12))
	fig.patch.set_facecolor('#E0E0E0')
	#BUTS
	TableBut = TableChoice.sort_values("Buts",ascending=False)
	ax1 = plt.subplot2grid((2, 2), (0, 0))
	ax1.bar(x=TableBut["Équipe"],height=TableBut["Buts"], color=st.ChampionshipColor[ChampionshipName])
	ax1.set_title("BUTS {Championship} 21/22".format(Championship=ChampionshipName), backgroundcolor="Black", color="White", fontweight="bold", pad=10)
	ax1.set_xlabel("EQUIPE" , fontweight="bold")
	ax1.set_ylabel("BUTS", fontweight="bold")
	ax1.set_ylim(0, TableBut["Buts"].max()+1)
	xlabels = TableBut["Équipe"]
	ax1.set_xticks(TableBut["Équipe"])
	ax1.set_xticklabels(xlabels, rotation=55,horizontalalignment="right",size=12,fontweight="bold")


	#XG
	TableButxG = TableChoice.sort_values("xG",ascending=False)
	ax2 = plt.subplot2grid((2, 2), (0, 1))
	ax2.bar(x=TableButxG["Équipe"],height=TableButxG["xG"], color=st.ChampionshipColor[ChampionshipName])
	ax2.set_title("xG {Championship}  21/22".format(Championship=ChampionshipName), backgroundcolor="Black", color="White", fontweight="bold", pad=10)
	ax2.set_xlabel("EQUIPE" , fontweight="bold")
	ax2.set_ylabel("xG", fontweight="bold")
	ax2.set_ylim(0, TableButxG["xG"].max()+1)
	xlabels = TableButxG["Équipe"]
	ax2.set_xticks(TableButxG["Équipe"])
	ax2.set_xticklabels(xlabels, rotation=55,horizontalalignment="right",size=12,fontweight="bold")


	#corrélation
	ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
	ax3 = sns.regplot(ax=ax3, x="xG",y="Buts",data=TableChoice, scatter_kws={'alpha':0.07}, color=st.ChampionshipColor[ChampionshipName])
	ax3.set_title("Corrélation Buts/xG {Championship}  21/22".format(Championship=ChampionshipName), backgroundcolor="Black", color="White", fontweight="bold", pad=10)
	ax3.set_xlabel("xG" , fontweight="bold")
	ax3.set_ylabel("BUTS", fontweight="bold")
	fig.tight_layout(pad=5.0)

	return fig


def BarplotTeamStat(df, Team1, Team2):

	barWidth =0.45

	columns = list(df.columns)
	#convert value string to float
	for i  in columns:
		df[i] = pd.to_numeric(df[i], downcast="float")

	df_01 = df.loc[:,df.loc[Team1] < 1]
	df_1 = df.loc[:,df.loc[Team1].between(1,10)]
	df_10 = df.loc[:,df.loc[Team1].between(10,50)]
	df_50 = df.loc[:,df.loc[Team1].between(50,100)]
	df_100 = df.loc[:,df.loc[Team1].between(100,500)]
	df_500 = df.loc[:,df.loc[Team1].between(500,1000)]
	df_1000 = df.loc[:,df.loc[Team1].between(1000,10000)]
	df_10000 = df.loc[:,df.loc[Team1] >= 10000]
	List_df = [df_01,df_1,df_10,df_50,df_100,df_500,df_1000,df_10000] 
	 
	list_figure = []
	for i in List_df:
		if len(i.loc[i.index[0]]) == 0:
			pass
		else:
			fig = plt.figure()
			colors = ['red', "black"]
			ax0 = plt.subplot2grid((1, 1), (0, 0))
			r1 = range(len(i.loc[i.index[0]]))
			r2 = [x + barWidth for x in r1]
			labels = list(i.columns)
			ind = np.arange(len(labels)) + barWidth/2
			b1 = ax0.bar(r1,i.loc[Team1], width = barWidth, color=colors[0])
			b2 = ax0.bar(r2,i.loc[Team2], width = barWidth, color=colors[1])
			ax0.set_xticks(ind,labels, rotation=55,horizontalalignment="right",size=12)
			plt.legend([b1,b2],list(i.index),loc='upper center',bbox_to_anchor=(1.03, 1))
			#Attach a text label above each bar displaying its height
			def autolabel(bars, Team):
				Iter = 0
				for bar in bars:
					#height = bar.get_height()
					heightList = i.loc[Team]
					height = heightList[labels[Iter]]
					Iter += 1
					ax0.text(bar.get_x() + bar.get_width()/2, 1.1*height,str(height),ha='center', va='bottom', size=6)
			autolabel(b1, Team1)
			autolabel(b2, Team2)
			list_figure.append(fig)

	return list_figure
