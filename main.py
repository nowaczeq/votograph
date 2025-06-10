import sys
import os
import numpy as np
import pandas as pd

##########################################
#######  SETTING UP THE DATAFRAMES  ######
##########################################

# Load the data frames
pres_system_df = pd.read_excel("raw_data/PresDb.xlsx")
parl_system_df = pd.read_excel("raw_data/NatLegDb.xlsx")

pres_iscompulsory_df = pd.read_excel("raw_data/CompulsoryVotPresDB.xlsx")
parl_iscompulsory_df = pd.read_excel("raw_data/CompulsoryVotParlDB.xlsx")

# Join all except voter turnout dataframes together
systems = pd.merge(pres_system_df, parl_system_df, on=["ISO2", "ISO3", "Country", "Year"], how="left")
iscompulsory = pd.merge(pres_iscompulsory_df, parl_iscompulsory_df, on=["ISO2", "ISO3", "Country", "Year"], how= "left")

# Remove year because it's useless and pissing me off
systems = systems.drop("Year", axis="columns")
iscompulsory = iscompulsory.drop("Year", axis="columns")

# Create the master data set
count_comp_df = pd.merge(systems, iscompulsory, on=["ISO2", "ISO3", "Country"], how= "left")
# print(count_comp_df.head(1))

# Handle the turnout dataframes
parl_turnout_df = pd.read_excel("raw_data/VotTurnoutParlDb.xlsx")
pres_turnout_df = pd.read_excel("raw_data/VotTurnoutPresDb.xlsx")
# print(parl_turnout_df.head(5))
# print(pres_turnout_df.head(5))

# Group the data by country with the average turnout
# Parliamentary turnout
parl_turnout_df["ParlVotTurn"] = (
    parl_turnout_df["ParlVotTurn"]
    .str.rstrip("%")
)
parl_turnout_df["ParlVotTurn"] = pd.to_numeric(parl_turnout_df["ParlVotTurn"], errors='coerce')

parl_turnout_grouped = (
    parl_turnout_df
    .groupby("Country", as_index=False)["ParlVotTurn"]
    .mean()
)
parl_turnout_grouped["Parliamentary Avg Turnout %"] = parl_turnout_grouped["ParlVotTurn"] / 100

# Presidential turnout
pres_turnout_df["PresVotTurn"] = (
    pres_turnout_df["PresVotTurn"]
    .str.rstrip("%")
)

pres_turnout_df["PresVotTurn"] = pd.to_numeric(pres_turnout_df["PresVotTurn"], errors='coerce')

pres_turnout_grouped = (
    pres_turnout_df
    .groupby("Country", as_index=False)["PresVotTurn"]
    .mean()
)

pres_turnout_grouped["Presidential Avg Turnout %"] = pres_turnout_grouped["PresVotTurn"] / 100
# print(parl_turnout_grouped.head(5))
# print(pres_turnout_grouped.head(5))
# print(parl_turnout_grouped.info())
# print(pres_turnout_grouped.info())

# Create the master dataframes
turnout_df = pd.merge(pres_turnout_df, parl_turnout_df, on=["Country", "ISO2", "ISO3", "Year"], how= "right")
avg_turnout_df = pd.merge(pres_turnout_grouped, parl_turnout_grouped, on=["Country"], how= "right")
print(avg_turnout_df.head(5))

# Create the master dataframe
master_df = pd.merge(avg_turnout_df, count_comp_df, on=["Country"], how="right")
master_df.drop(columns=["PresVotTurn", "ParlVotTurn"])

# Rename the columns in the master dataframe
master_df.rename(columns={
    "Country": "Country",
    "PresVotTurn": "PresTurnout",
    "Presidential Avg Turnout %": "%PresTurnout",
    "ParlVotTurn": "ParlTurnout",
    "Parliamentary Avg Turnout %": "%ParlTurnout",
    "ISO2": "ISO2",
    "ISO3": "ISO3",
    "PresSystem": "PresVotingSystem",
    "ParlSystem": "ParlVotingSystem",
    "PresComp": "PresCompulsory",
    "ParlComp": "ParlCompulsory"
})
# print(master_df.info())

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
# print(parl_comp)
# print(pres_comp)

# Get information about turnout statistics
# print(avg_turnout_df.describe())
# print(turnout_df.describe())
print(master_df[master_df["ParlComp"].notnull()].describe())

##########################################
##########  INFERENTIAL STATS  ###########
##########################################