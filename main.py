import sys
import os
import numpy as np
import pandas as pd

##########################################
#######  SETTING UP THE DATAFRAMES  ######
##########################################

# Load the data frames
pres_system_df = pd.read_excel("PresDb.xlsx")
parl_system_df = pd.read_excel("NatLegDb.xlsx")

pres_iscompulsory_df = pd.read_excel("CompulsoryVotPresDB.xlsx")
parl_iscompulsory_df = pd.read_excel("CompulsoryVotParlDB.xlsx")

# Join all except voter turnout dataframes together
systems = pd.merge(pres_system_df, parl_system_df, on=["ISO2", "ISO3", "Country", "Year"], how="left")
iscompulsory = pd.merge(pres_iscompulsory_df, parl_iscompulsory_df, on=["ISO2", "ISO3", "Country", "Year"], how= "left")

# Remove year because it's useless and pissing me off
systems = systems.drop("Year", axis="columns")
iscompulsory = iscompulsory.drop("Year", axis="columns")

# Create the master data set
master_df = pd.merge(systems, iscompulsory, on=["ISO2", "ISO3", "Country"], how= "left")
# print(master_df.head(1))

# Handle the turnout dataframes
parl_turnout_df = pd.read_excel("VotTurnoutParlDb.xlsx")
pres_turnout_df = pd.read_excel("VotTurnoutPresDb.xlsx")
# print(parl_turnout_df.head(5))
# print(pres_turnout_df.head(5))

# Drop the "year" column
parl_turnout_df.drop(columns=["year"])
pres_turnout_df.drop(columns=["Year"])

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

# Create the master turnout dataframe
turnout_df = pd.merge(pres_turnout_grouped, parl_turnout_grouped, on=["Country"], how= "right")
print(turnout_df.info())


##########################################
############  DATA ANALYSIS  #############
##########################################

# Count of voting systems in parliamentary and presidential elections
parl_system_count = master_df["ParlSystem"].value_counts()
pres_system_count = master_df["PresSystem"].value_counts()
# print(parl_system_count)
# print(pres_system_count)

# Count of countries where elections are compulsory
parl_comp = master_df["ParlComp"].value_counts()
pres_comp = master_df["PresComp"].value_counts()
# print(parl_comp)
# print(pres_comp)

##########################################
##########  INFERENTIAL STATS  ###########
##########################################