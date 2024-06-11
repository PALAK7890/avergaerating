import pandas as pd 
import plotly.figure_factory as ff

df=pd.read_csv("dataproject.csv")

brands=df["Mobile Brand"].tolist()
rating=df["Avg Rating"].tolist()

fig=ff.create_distplot([rating],['mobile brands average rating'],show_hist=False)
fig.show()

