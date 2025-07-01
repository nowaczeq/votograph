# Match each election in the voting master database to closest available data from the GapMinder set of dataframes
import pandas as pd
import numpy as np
import setup_idea
import setup_gapminder 

def match_elections_to_data(df_elections: pd.DataFrame, country_data: dict):
    if not isinstance(df_elections, pd.DataFrame) or not isinstance(country_data, dict):
        raise ValueError(f"Error in matchmaker function: function expected pandas Dataframe, got {type(df_elections)} and a dictionary, got {type(country_data)} ")

    # PREPARE THE DATA FOR SORTING
    # Rename the columns
    df_elections = df_elections.rename(columns={"Country": "country", "Year": "year"})

    # Convert to uniform data types
    df_elections['year'] = pd.to_datetime(df_elections['year'], errors='coerce').dt.year
    df_elections = df_elections.dropna(subset=['year'])
    df_elections['year'] = df_elections['year'].astype(int)

    # Get the gapminder datasets from the passed dict
    labour_participation_df = country_data["labour_participation"].rename(columns={"geo": "ISO3", "time": "year"})
    ppp_gdp_per_capita_df = country_data["ppp_gdp_per_capita"].rename(columns={"geo": "ISO3", "time": "year"})
    democracy_score_df = country_data["democracy_score"].rename(columns={"geo": "ISO3", "time": "year"})
    economic_growth_df = country_data["economic_growth"].rename(columns={"geo": "ISO3", "time": "year"})
    hdi_df = country_data["hdi"].rename(columns={"geo": "ISO3", "time": "year"})
    sex_ratio_df = country_data["sex_ratio"].rename(columns={"geo": "ISO3", "time": "year"})
    income_pp_df = country_data["income_pp"].rename(columns={"geo": "ISO3", "time": "year"})


    # Perform outer merge on gapminder dataframes to preserve data for respective years
    gm = pd.merge(labour_participation_df, ppp_gdp_per_capita_df, on=['year', 'ISO3'], how='outer')
    gm = pd.merge(gm, economic_growth_df, on=['year', 'ISO3'], how='outer')
    gm = pd.merge(gm, democracy_score_df, on=['year', 'ISO3'], how='outer')
    gm = pd.merge(gm, hdi_df, on=['year', 'ISO3'], how='outer')
    gm = pd.merge(gm, sex_ratio_df, on=['year', 'ISO3'], how='outer')
    gm = pd.merge(gm, income_pp_df, on=['year', 'ISO3'], how='outer')

    df_elections_sorted = df_elections.sort_values(['ISO3', 'year']).reset_index(drop=True)
    df_elections_sorted['ISO3'] = df_elections_sorted['ISO3'].str.lower()
    df_elections_sorted = df_elections_sorted.drop_duplicates(subset=['ISO3', 'year'])

    gm_sorted = gm.sort_values(['ISO3', 'year'], kind='mergesort').reset_index(drop=True)

    # Sort by 'year' then 'ISO3', since 'year' is the 'on' key
    df_elections_sorted = df_elections_sorted.sort_values(['year', 'ISO3']).reset_index(drop=True)
    gm_sorted = gm_sorted.sort_values(['year', 'ISO3']).reset_index(drop=True)

    # Now merge_asof should work
    output = pd.merge_asof(
        df_elections_sorted,
        gm_sorted,
        on='year',
        by='ISO3',
        direction='nearest',
        suffixes=('', '_before')
    )

    return output


if __name__ == "__main__":
    country_data = setup_gapminder.setup_dfs()
    df_elections = setup_idea.setup_dfs()['parliamentary_master']
    match_elections_to_data(df_elections, country_data)