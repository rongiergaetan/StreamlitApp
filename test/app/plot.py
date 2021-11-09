import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import setting as st



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