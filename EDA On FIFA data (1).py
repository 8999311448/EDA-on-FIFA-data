#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


#loading the fifa 20 dataset
fifa=pd.read_csv(r'C:\Users\saksh\Downloads\players_20.csv')


# In[3]:


#having a glance at the first 5 records of the dataset
fifa.head()


# In[4]:


#print the column names in the dataset
for col in fifa.columns:
    print(col)


# In[5]:


#no of records in dataset
fifa.shape


# In[6]:


#frequency of players belonging to each nationality
fifa['nationality'].value_counts()


# In[7]:


#frequency of players belonging to first 10 nationality
fifa['nationality'].value_counts()[0:10]


# In[8]:


#bar graph to visualize the data of frequency of players belonging to first 10 nationality
plt.figure(figsize=(5,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()), list(fifa['nationality'].value_counts()[0:5]), color=['red', 'blue', 'yellow', 'purple', 'green'])
plt.title('Nationality')
plt.ylabel('Frequency')
plt.xlabel('Nation')
plt.show()


# In[9]:


player_salary= fifa[['short_name', 'wage_eur']]
player_salary.head()


# In[10]:


#sort the values to check highest paid player
player_salary=player_salary.sort_values(by=['wage_eur'], ascending= False)


# In[11]:


#having a glance at player_salary data after sorting
player_salary.head()


# In[12]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'][0:5]), list(player_salary['wage_eur'][0:5]), color=['blue', 'yellow', 'red', 'purple', 'pink'])
plt.title('Wage earned by each player')
plt.xlabel('Players')
plt.ylabel('salary')
plt.show()


# In[13]:


#players belong to Germany
fifa['nationality']=='Germany'


# In[14]:


#storing the dataset of players belonging to Germany in individual dataset
Germany= fifa[fifa['nationality']=='Germany']


# In[15]:


#extract the data from Germany 
Germany.head()


# In[16]:


#tallest player in Germany
Germany.sort_values(by=['height_cm'], ascending= False).head()


# In[17]:


#Players in Germany with maximum weight
Germany.sort_values(by=['weight_kg'], ascending= False).head()


# In[18]:


#Sort players in Germany according to wages 
Germany.sort_values(by=['wage_eur'], ascending= False).head()


# In[19]:


#extract the name of the players in Germany according to wages
Germany[['short_name', 'wage_eur']].sort_values(by=['wage_eur'], ascending=False).head()


# In[20]:


fifa['club'].value_counts()


# In[21]:


#Save the data of Players belonging to Barcelona club to individual Dataframe
Barcelona= fifa[ fifa['club']== 'FC Barcelona']


# In[22]:


#having a glance at first 5 record of Barcelona
Barcelona.head()


# In[23]:


#highest earning players of Barcelona
Barcelona.sort_values(by=('wage_eur'), ascending= False).head()


# In[24]:


Barcelona['nationality'].value_counts()


# In[45]:


#Frequency of nationality of players in Barcelona
plt.figure(figsize=(8,8))
plt.pie(list(Barcelona['nationality'].value_counts()), labels=list(Barcelona['nationality'].value_counts().keys()), autopct='%0.1f%%')
plt.show()


# In[25]:


FC=Barcelona[['short_name', 'wage_eur']].sort_values(by=('wage_eur'), ascending= False)


# In[26]:


FC.head()


# In[27]:


#data visualization for highest earning players of Barcelona
plt.figure(figsize=(7,5))
plt.bar(list(FC['short_name'][0:5]), list(FC['wage_eur'][0:5]), color='pink')
plt.xlabel('Players')
plt.ylabel('wages')
plt.show


# In[28]:


#rating for best shooting skills
player_shooting= fifa[['short_name', 'shooting', 'nationality', 'club']]


# In[29]:


player_shooting.sort_values(by=['shooting'], ascending= False).head()


# In[58]:


#statistical analysis
mean_shooting = np.mean(player_shooting['shooting'])
mean_shooting


# In[30]:


#Extract the data of rating for defending skills
player_defending= fifa[['short_name','defending','nationality', 'club']]


# In[31]:


#extract first five sorted records w.r.t highest defending skills
player_defending.sort_values(by=['defending'], ascending= False).head()


# In[60]:


#statistical analysis
mean_defending = np.mean(player_defending['defending'])
mean_defending


# In[32]:


#Save the data of Players belonging to Real Madrid club to individual Dataframe
real_madrid= fifa[ fifa['club']== 'Real Madrid']


# In[33]:


#having a glance at first 5 record of Real Madrid
real_madrid.head()


# In[34]:


#highest earning players of Real Madrid
real_madrid.sort_values(by=('wage_eur'), ascending= False).head()


# In[35]:


real_madrid['nationality'].value_counts()


# In[46]:


#Frequency of nationality of players in Barcelona
plt.figure(figsize=(8,8))
plt.pie(list(real_madrid['nationality'].value_counts()), labels=list(real_madrid['nationality'].value_counts().keys()), autopct='%0.1f%%')
plt.show()


# In[36]:


RM=real_madrid[['short_name', 'wage_eur']].sort_values(by=('wage_eur'), ascending= False)


# In[37]:


RM.head()


# In[38]:


#data visualization for highest earning players of Real madrid
plt.figure(figsize=(7,5))
plt.bar(list(RM['short_name'][0:5]), list(RM['wage_eur'][0:5]), color='cyan')
plt.xlabel('Players')
plt.ylabel('wages')
plt.show


# In[39]:


fifa['gk_speed'].value_counts().head()


# In[55]:


Total_gk_speed=np.sum(fifa['gk_speed'])
Total_gk_speed


# In[48]:


fifa['lwb'].value_counts()


# In[54]:


#data visualization for frequency of a particular left Wing back position in the dataset
plt.figure(figsize=(12,12))
plt.plot(list(fifa['lwb'].value_counts()[0:10]), list(fifa['lwb'].value_counts()[0:10].keys()), label='Line Chart')
plt.show()


# In[ ]:




