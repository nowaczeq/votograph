import numpy as np
import pandas as pd
import statsmodels.api as sm
import setup_idea
import setup_gapminder
import matchmaker

##########################################
#######  SETTING UP THE DATAFRAMES  ######
##########################################

# Set up idea dataframes
idea_dfs = setup_idea.setup_dfs()
idea_parliamentary_master = idea_dfs["parliamentary_master"]
idea_presidential_master = idea_dfs["presidential_master"]
idea_master_df = idea_dfs["master"]
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
labour_participation_df = gapminder_dfs["labour_participation"]
ppp_gdp_per_capita_df = gapminder_dfs["ppp_gdp_per_capita"]
democracy_score_df = gapminder_dfs["democracy_score"]
economic_growth_df = gapminder_dfs["economic_growth"]
hdi_df = gapminder_dfs["hdi"]
sex_ratio_df = gapminder_dfs["sex_ratio"]
income_pp_df = gapminder_dfs["income_pp"]
gapminder_master_df = gapminder_dfs["master"]

# Delete the master dataframe to allow easier looping over all 
del gapminder_dfs["master"]

# Merge the two sources into a master dataframe, containing average data for each country
gapminder_master_df["country"] = gapminder_master_df["country"].str.upper()
parliamentary_master_with_averages = pd.merge(
    idea_parliamentary_master, gapminder_master_df, 
    how="left", left_on="ISO3", right_on="country")

presidential_master = pd.merge(
    idea_presidential_master, gapminder_master_df,
    how="left", left_on="ISO3", right_on="country")

# This isn't good enough, we need to associate each election to the gapminder data separately
# not the averages, which is the case here

# Match the individual election to the closest possible data
print(idea_parliamentary_master.head(1))
print(labour_participation_df.head(1))
# master = matchmaker.match_elections_to_data(idea_parliamentary_master, gapminder_dfs)

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
# print(idea_master_df["PresSystem"].value_counts())

# Get information about turnout
# print(idea_master_df.head())

# President: mean turnout for each voting system
mean_system_turnout_pres = idea_master_df.groupby('PresSystem', as_index=False)['Presidential Avg Turnout %'].mean()
# Parliament: mean turnout for each voting system
mean_system_turnout_parl = idea_master_df.groupby('ParlSystem', as_index=False)['Parliamentary Avg Turnout %'].mean()

# President: mean turnout for compulsory vs non-compulsory
mean_comp_turnout_pres = idea_master_df.groupby('PresComp', as_index=False)['Presidential Avg Turnout %'].mean()
# Parliament: mean turnout for compulsory vs non-compulsory
mean_comp_turnout_parl = idea_master_df.groupby('ParlComp', as_index=False)['Parliamentary Avg Turnout %'].mean()

# print(idea_master_df.head())

##########################################
##########  INFERENTIAL STATS  ###########
##########################################
