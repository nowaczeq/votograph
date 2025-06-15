# Setup dataframes imported from idea datasets
import numpy as np
import pandas as pd

def setup_dfs():
    # Load the data frames
    pres_system_df = pd.read_excel("raw_data_idea/PresDb.xlsx")
    parl_system_df = pd.read_excel("raw_data_idea/NatLegDb.xlsx")

    pres_iscompulsory_df = pd.read_excel("raw_data_idea/CompulsoryVotPresDB.xlsx")
    parl_iscompulsory_df = pd.read_excel("raw_data_idea/CompulsoryVotParlDB.xlsx")

    # Join all except voter turnout dataframes together
    systems = pd.merge(pres_system_df, parl_system_df, on=["ISO2", "ISO3", "Country", "Year"], how="left")
    iscompulsory = pd.merge(pres_iscompulsory_df, parl_iscompulsory_df, on=["ISO2", "ISO3", "Country", "Year"], how= "left")

    # Remove year because it's useless and pissing me off
    systems = systems.drop("Year", axis="columns")
    iscompulsory = iscompulsory.drop("Year", axis="columns")

    # Create the master data set
    count_comp_df = pd.merge(systems, iscompulsory, on=["ISO2", "ISO3", "Country"], how= "left")

    # Handle the turnout dataframes
    parl_turnout_df = pd.read_excel("raw_data_idea/VotTurnoutParlDb.xlsx")
    pres_turnout_df = pd.read_excel("raw_data_idea/VotTurnoutPresDb.xlsx")

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

    # Create the master dataframes
    turnout_df = pd.merge(pres_turnout_df, parl_turnout_df, on=["Country", "ISO2", "ISO3", "Year"], how= "right")
    avg_turnout_df = pd.merge(pres_turnout_grouped, parl_turnout_grouped, on=["Country"], how= "right")
    avg_turnout_df.drop(columns=["PresVotTurn", "ParlVotTurn"], inplace=True)
    # print(avg_turnout_df.head(5))

    # Create the master dataframe
    master_df = pd.merge(avg_turnout_df, count_comp_df, on=["Country"], how="right")

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


    # Creating a master data frame with information for each election
    # turnout - parl/pres turnout
    # sys - pres/parl system
    # comp - iscompulsory

    # Master dataframe for parliamentary elections
    parl_system_df.drop(columns="Year", inplace=True)
    parl_iscompulsory_df.drop(columns="Year", inplace=True)
    tmp = pd.merge(parl_turnout_df, parl_system_df, on=["Country", "ISO2", "ISO3"], how="left")
    parliamentary_master = pd.merge(tmp, parl_iscompulsory_df, on=["Country", "ISO2", "ISO3"], how="left")
    # print(parliamentary_master.head(5))

    # Master dataframe for presidential elections
    pres_system_df.drop(columns="Year", inplace=True)
    pres_iscompulsory_df.drop(columns="Year", inplace=True)
    tmp = pd.merge(pres_turnout_df, pres_system_df, on=["Country", "ISO2", "ISO3"], how="left")
    presidential_master = pd.merge(tmp, pres_iscompulsory_df, on=["Country", "ISO2", "ISO3"], how="left")

    # Optionally view the master dataframes
    # print(parliamentary_master.head(5))
    # print(presidential_master.head(5))
    # print(master_df.head(5))

    # Package the dataframes into a dictionary
    output = {
        "parliamentary_master": parliamentary_master,
        "presidential_master": presidential_master,
        "master": master_df,
        "pres_system_df": pres_system_df,
        "parl_system_df": parl_system_df,
        "pres_iscompulsory_df": pres_iscompulsory_df,
        "parl_iscompulsory_df": parl_iscompulsory_df,
        "systems": systems,
        "iscompulsory": iscompulsory,
        "parl_turnout_df": parl_turnout_df,
        "pres_turnout_df": pres_turnout_df,
        "pres_turnout_grouped": pres_turnout_grouped,
        "parl_turnout_grouped": parl_turnout_grouped,
        "turnout_df": turnout_df,
        "count_comp_df": count_comp_df,
        "avg_turnout_df": avg_turnout_df
    }
    
    # Return the dictionary
    return output