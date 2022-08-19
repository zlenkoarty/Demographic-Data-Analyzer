import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read data from CSV file
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
#Add an overweight column to the data. To determine if a person is overweight, 
#first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. 
#If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

df['overweight'] = (df['weight'] / (df['height']/100)**2).apply(lambda x: 1 if x > 25 else 0)

#Normalize the data by making 0 always good and 1 always bad. 
#If the value of cholesterol or gluc is 1, make the value 0. 
#If the value is more than 1, make the value 1.

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
df['gluc'] =df['gluc'].apply(lambda x:0 if x==1 else 1)

#Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot().
#The dataset should be split by 'Cardio' so there is one chart for each cardio value. 
#The chart should look like examples/Figure_1.png.


df_cat = pd.melt(df, id_vars = 'cardio',value_vars = ['alco', 'active','cholesterol', 'gluc', 'overweight','smoke'])


df_cat.head()
