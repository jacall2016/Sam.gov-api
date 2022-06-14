import pandas as pd

df = pd.read_csv ('data_files\oppurtunityTracker.csv')

#df.assign(opportunitiesData=df.opportunitiesData.str.split(','))

#df.opportunitiesData.str.split(expand=True,)

opp_CSV = df.opportunitiesData.str.split(expand=True,)

#opp_CSV.to_('data_files\oppData.csv')
opp_CSV.to_excel('data_files\oppData.xlsx')

print(opp_CSV)
