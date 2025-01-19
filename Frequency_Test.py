#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from collections import Counter
import csv
import os
from scipy.stats import chi2_contingency
import scipy.stats as stats


# ## Cards

# In[23]:


data_file=r"C:\Users\Ai Team2\Documents\dataset1\df_Small.csv"
start_row=0
"""increments = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
        20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,
        200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000,
        2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000,
        20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000]"""

chi2_results_list = []
increments=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
for size in increments:
    chunk= pd.read_csv(data_file , skiprows=start_row, nrows= size)
    df_card=chunk[["card"]]
    # Split the 'card' column into separate columns
    split_cards = df_card['card'].str.split(',', expand=True)
    #value_counts
    melted = split_cards.melt(var_name='position', value_name='card')
    melted=melted.groupby(['card', 'position'] , sort=True).size().unstack()
    
    # Save the resulting DataFrame to a CSV file
    output_file = f"card_frequencies_{size}.csv"  
    melted.to_csv(output_file)
    print(f"Saved card frequencies for sample size {size} to {output_file}")

     # Calculate the Chi-square test for the contingency table
    chi2_stat, p_value, dof, expected = chi2_contingency(melted)
    
    # Append the results to the list
    chi2_results_list.append({ 'Sample Size': size, 'Chi-square Statistic': chi2_stat , 'P-value': p_value } ) 
    
    # Print the results
    #print(f"Chi-square statistic for sample size {size}: {chi2_stat}")
    #print(f"P-value for sample size {size}: {p_value}")


# Convert the results list to a DataFrame
chi2_results_cards = pd.DataFrame(chi2_results_list)

# Save all Chi-square results to a single CSV file
chi2_results_cards.to_csv("chi2_results_cards.csv", index=False)


# ## Dice 

# In[28]:


data_file=r"C:\Users\Ai Team2\Documents\dataset1\df_Small.csv"
increments=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

chi2_results_list=[]
start_row=0

for size in increments:
    chunk= pd.read_csv(data_file , skiprows=start_row, nrows= size)
    df_Dice=chunk[["dice"]]
    # Calculate value counts
    value_counts = df_Dice.value_counts() 
    # Convert the Series to a DataFrame
    df_value_counts = value_counts.reset_index()
    # Rename the columns
    df_value_counts.columns = ['Outcome', 'Frequency']

    #Save the resulting DataFrame to a CSV file
    output_file = f"Dice_frequencies_{size}.csv" 
    df_value_counts.to_csv(output_file)
    print(f"Saved Dice frequencies for sample size {size} to {output_file}")

    # Prepare the observed and expected frequencies for the Chi-Square test
    observed_freq = df_value_counts['Frequency']
    expected_freq= ( observed_freq.sum() / len(observed_freq) ) 
    expected_frequencies = [expected_freq] * len(observed_freq) 
    

    chi2_stat, p_value = stats.chisquare(observed_freq, expected_frequencies)   
    
    # Append the results to the list
    chi2_results_list.append({ 'Sample Size': size, 'Chi-square Statistic': chi2_stat , 'P-value': p_value } ) 

# Convert the results list to a DataFrame
chi2_results_Dice = pd.DataFrame(chi2_results_list)

# Save all Chi-square results to a single CSV file
chi2_results_Dice.to_csv("chi2_results_Dice.csv", index=False)


# ## Lotto 

# In[32]:


data_file=r"C:\Users\Ai Team2\Documents\dataset1\df_Small.csv"
increments=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

chi2_results_list=[]
start_row=0

for size in increments:
    chunk= pd.read_csv(data_file , skiprows=start_row, nrows= size)
    df_lotto=chunk[['lotoo']]
    df_lotto= df_lotto['lotoo'].str.split(',', expand=True)
    #creating Frequency matrix
    df_lotto=df_lotto.astype(int)
    melted = df_lotto.melt(var_name='position', value_name='Number')
    melted=melted.groupby(['Number', 'position'] , sort=True).size().reset_index(name='Count')
    frequency_matrix = melted.pivot(index='Number', columns='position', values='Count')
    
    # Save the resulting DataFrame to a CSV file
    output_file = f"lotto_frequencies_{size}.csv"  
    frequency_matrix.to_csv(output_file)
    print(f"Saved lotto frequencies for sample size {size} to {output_file}")

    # Calculate the Chi-square test for the contingency table
    chi2_stat, p_value, _, _ = chi2_contingency(frequency_matrix)
    
    # Append the results to the list
    chi2_results_list.append({ 'Sample Size': size, 'Chi-square Statistic': chi2_stat , 'P-value': p_value } ) 


# Convert the results list to a DataFrame
chi2_results_lotto = pd.DataFrame(chi2_results_list)

# Save all Chi-square results to a single CSV file
chi2_results_lotto.to_csv("chi2_results_lotto.csv", index=False)


# In[ ]:




