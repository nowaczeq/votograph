import numpy as np
import pandas as pd
import statsmodels.api as sm
import setup_idea
import setup_gapminder

##########################################
#######  SETTING UP THE DATAFRAMES  ######
##########################################

# Set up idea dataframes
idea_dfs = setup_idea.setup_dfs()
parliamentary_master = idea_dfs["parliamentary_master"]
presidential_master = idea_dfs["presidential_master"]
master_df = idea_dfs["master"]
pres_system_df = idea_dfs["pres_system_df"]
parl_system_df = idea_dfs["parl_system_df"]
pres_iscompulsory_df = idea_dfs["pres_iscompulsory_df"]
parl_iscompulsory_df = idea_dfs["parl_iscompulsory_df"]
systems = idea_dfs["systems"]
iscompulsory = idea_dfs["iscompulsory"]
parl_turnout_df = idea_dfs["parl_turnout_df"]
pres_turnout_df = idea_dfs["pres_turnout_df"]
parl_turnout_grouped = idea_dfs["parl_turnout_grouped"]
pres_turnout_grouped = idea_dfs["pres_turnout_grouped"]
turnout_df = idea_dfs["turnout_df"]
count_comp_df = idea_dfs["count_comp_df"]
avg_turnout_df = idea_dfs["avg_turnout_df"]

# Set up GapMinder dataframes
gapminder_dfs = setup_gapminder.setup_dfs()

##########################################
############  DATA ANALYSIS  #############
##########################################

# Count of voting systems in parliamentary and presidential elections
parl_system_count = count_comp_df["ParlSystem"].value_counts()
pres_system_count = count_comp_df["PresSystem"].value_counts()
# print(parl_system_count)
# print(pres_system_count)

# Count of countries where elections are compulsory
parl_comp = count_comp_df["ParlComp"].value_counts()
pres_comp = count_comp_df["PresComp"].value_counts()


# Get information about turnout statistics
# print(avg_turnout_df.describe())
# print(turnout_df.describe())
# print(master_df["PresSystem"].value_counts())

# Get information about turnout
# print(master_df.head())

# President: mean turnout for each voting system
mean_system_turnout_pres = master_df.groupby('PresSystem', as_index=False)['Presidential Avg Turnout %'].mean()
# Parliament: mean turnout for each voting system
mean_system_turnout_parl = master_df.groupby('ParlSystem', as_index=False)['Parliamentary Avg Turnout %'].mean()

# President: mean turnout for compulsory vs non-compulsory
mean_comp_turnout_pres = master_df.groupby('PresComp', as_index=False)['Presidential Avg Turnout %'].mean()
# Parliament: mean turnout for compulsory vs non-compulsory
mean_comp_turnout_parl = master_df.groupby('ParlComp', as_index=False)['Parliamentary Avg Turnout %'].mean()

# print(master_df.head())

##########################################
##########  INFERENTIAL STATS  ###########
##########################################