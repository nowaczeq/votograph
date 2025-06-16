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
    for value in country_data.values():
        value = value.rename(columns={"geo": "country", "time": "year"})

    # Convert to uniform data types
    df_elections['year'] = pd.to_datetime(df_elections['year'], errors='coerce').dt.year
    df_elections = df_elections.dropna(subset=['year'])
    df_elections['year'] = df_elections['year'].astype(int)

    # Get the gapminder datasets from the passed dict
    labour_participation_df = country_data["labour_participation"].rename(columns={"geo": "country", "time": "year"})
    ppp_gdp_per_capita_df = country_data["ppp_gdp_per_capita"].rename(columns={"geo": "country", "time": "year"})
    democracy_score_df = country_data["democracy_score"].rename(columns={"geo": "country", "time": "year"})
    economic_growth_df = country_data["economic_growth"].rename(columns={"geo": "country", "time": "year"})
    hdi_df = country_data["hdi"].rename(columns={"geo": "country", "time": "year"})
    sex_ratio_df = country_data["sex_ratio"].rename(columns={"geo": "country", "time": "year"})
    income_pp_df = country_data["income_pp"].rename(columns={"geo": "country", "time": "year"})


    # Perform outer merge on gapminder dataframes to preserve data for respective years
    gm = pd.merge(labour_participation_df, ppp_gdp_per_capita_df, on=['year', 'country'], how='outer')
    gm = pd.merge(gm, economic_growth_df, on=['year', 'country'], how='outer')
    gm = pd.merge(gm, democracy_score_df, on=['year', 'country'], how='outer')
    gm = pd.merge(gm, hdi_df, on=['year', 'country'], how='outer')
    gm = pd.merge(gm, sex_ratio_df, on=['year', 'country'], how='outer')
    gm = pd.merge(gm, income_pp_df, on=['year', 'country'], how='outer')

    # Sort values by year, reset indexes
    gm = gm.sort_values(['year', 'country']).reset_index(drop=True)
    df_elections = df_elections.sort_values(['year', 'country']).reset_index(drop=True)

    # Create copies of gm for merging
    gm_before = gm.copy()
    gm_before['new_year'] = gm_before['year']
    gm_before = gm_before.rename(columns={'new_year': 'year_before'})
    gm_after = gm.copy()
    gm_after['new_year'] = gm_before['year']
    gm_after = gm_after.rename(columns={'new_year': 'year_after'})
    # Merge to get information before or on / after election year
    df_before = pd.merge_asof(
        df_elections,
        gm_before,
        on='year',
        by='country',
        direction='backward',
        suffixes=('', '_before')
    )

    df_after = pd.merge_asof(
        df_elections,
        gm_after,
        on='year',
        by='country',
        direction='forward',
        suffixes=('', '_after')
    )

    # Get the differences between the estimated years and the actual year
    before_diff = (df_elections["year"] - df_before["year_before"]).abs()
    after_diff  = (df_elections["year"] - df_after["year_after"]).abs()

    # Change the year to the closest year available
    df_elections["year"] = np.where(before_diff <= after_diff,
                                df_before["year_before"],
                                df_after["year_after"])

    return

    # For each election, compare whether the data from 'backward' or 'forward' directions are closer and apply those
    df_combined = df_before.copy()
    before_diff = abs(df_before['year'] - df_before['year']) # Backward merge difference between election year and assigned data
    after_diff = abs(df_after['year'] - df_after['year'])     # Forward merge difference between election year and assigned data

    # Create a mask for assignment
    mask = after_diff < before_diff
    for col in gm.columns:
        if col not in ['country', 'year']:
            df_combined.loc[mask, col] = df_after.loc[mask, col + '_after']

    print(df_combined.head(10))

    return

if __name__ == "__main__":
    country_data = setup_gapminder.setup_dfs()
    df_elections = setup_idea.setup_dfs()['parliamentary_master']
    match_elections_to_data(df_elections, country_data)