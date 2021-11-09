import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sys

TablePass = pd.read_csv(sys.argv[1])
ChampionshipName = sys.argv[1].split(".")[2].split("_")[1]
ChampionshipColor = {"Bundesliga":"#006400","PL":"#6495ED","liga":"#EEB422","SerieA":"#9400D3","L1":"#DC143C"}


def StatButs(TablePass):
	fig = plt.figure(figsize=(12,12))
	fig.patch.set_facecolor('#E0E0E0')
	#BUTS
	TablePassBut = TablePass.sort_values("Buts",ascending=False)
	ax1 = plt.subplot2grid((2, 2), (0, 0))
	ax1.bar(x=TablePassBut["Équipe"],height=TablePassBut["Buts"], color=ChampionshipColor[ChampionshipName])
	ax1.set_title("BUTS {Championship} 21/22".format(Championship=ChampionshipName), backgroundcolor="Black", color="White", fontweight="bold", pad=10)
	ax1.set_xlabel("EQUIPE" , fontweight="bold")
	ax1.set_ylabel("BUTS", fontweight="bold")
	ax1.set_ylim(0, TablePassBut["Buts"].max()+1)
	xlabels = TablePassBut["Équipe"]
	ax1.set_xticks(TablePassBut["Équipe"])
	ax1.set_xticklabels(xlabels, rotation=45,horizontalalignment="right")


	#XG
	TablePassxG = TablePass.sort_values("xG",ascending=False)
	ax2 = plt.subplot2grid((2, 2), (0, 1))
	ax2.bar(x=TablePassxG["Équipe"],height=TablePassxG["xG"], color=ChampionshipColor[ChampionshipName])
	ax2.set_title("xG {Championship}  21/22".format(Championship=ChampionshipName), backgroundcolor="Black", color="White", fontweight="bold", pad=10)
	ax2.set_xlabel("EQUIPE" , fontweight="bold")
	ax2.set_ylabel("xG", fontweight="bold")
	ax2.set_ylim(0, TablePassxG["xG"].max()+1)
	xlabels = TablePassxG["Équipe"]
	ax2.set_xticks(TablePassxG["Équipe"])
	ax2.set_xticklabels(xlabels, rotation=45,horizontalalignment="right")


	#corrélation
	ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
	ax3 = sns.regplot(ax=ax3, x="xG",y="Buts",data=TablePass, scatter_kws={'alpha':0.07}, color=ChampionshipColor[ChampionshipName])
	ax3.set_title("Corrélation Buts/xG {Championship}  21/22".format(Championship=ChampionshipName), backgroundcolor="Black", color="White", fontweight="bold", pad=10)
	ax3.set_xlabel("xG" , fontweight="bold")
	ax3.set_ylabel("BUTS", fontweight="bold")
	fig.tight_layout(pad=5.0)

	return fig
figbut = StatButs(TablePass)
plt.show(figbut)
