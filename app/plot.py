import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import setting as st
import numpy as np



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
			b1 = ax0.bar(r1,i.loc[Team1], width = barWidth, color=colors[0], label=Team1)
			b2 = ax0.bar(r2,i.loc[Team2], width = barWidth, color=colors[1], label=Team2)
			#ax0.set_xticks(ind,labels)
			ax0.set_xticks(ind)
			ax0.set_xticklabels(labels,rotation=30,horizontalalignment="right",size=10,verticalalignment="top")
			ax0.legend(loc='upper center',bbox_to_anchor=(1.06, 1))
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
