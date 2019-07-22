# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here

data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'},inplace=True)

print(data.head(10))



# --------------
#Code starts here







data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',(np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both')))
# data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both')

better_event = 'Summer'
print(better_event)












# --------------
#Code starts here


top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries = top_countries.iloc[:-1,:]

def top_ten(df,col):
    country_list =[]
    top = df.nlargest(10,col)
    print(top)
    country_list = list(top['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')    
top_10 = top_ten(top_countries,'Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print(common)












# --------------
#Code starts here



summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1)

ax_1.plot(summer_df['Country_Name'],summer_df['Total_Summer'])

ax_2.plot(winter_df['Country_Name'],winter_df['Total_Summer'])

ax_3.plot(top_df['Country_Name'],top_df['Total_Summer'])




# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()]['Country_Name'].values[0]
# summer_country_gold = summer_df['Country_Name'].get(key = summer_df['Golden_Ratio'].max())
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max()]['Country_Name'].values[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max()]['Country_Name'].values[0]









# --------------
#Code starts here



data_1 = data.iloc[:-1,:]
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points']==most_points]['Country_Name'].values[0]
print(best_country)




# --------------
#Code starts here


best = data[data['Country_Name']==best_country]
print(best)

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)





