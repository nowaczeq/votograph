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