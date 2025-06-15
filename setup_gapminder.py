# Setup dataframes from GapMinder datasets
import numpy as np
import pandas as pd


def setup_dfs():
    output = {}

    GLOBALIS_FP = "raw_data_gapminder\\ddf--datapoints--"

    # Load the datasets
    country_data = pd.read_csv(GLOBALIS_FP + "entities--geo--country.csv")
    labour_participation = pd.read_csv(GLOBALIS_FP + "aged_15plus_labour_force_participation_rate_percent--by--geo--time.csv")
    ppp_gdp_per_capita = pd.read_csv(GLOBALIS_FP + "alternative_gdp_per_capita_ppp_wb--by--geo--time.csv")
    democracy_score = pd.read_csv(GLOBALIS_FP + "democracy_score_use_as_color--by--geo--time.csv")
    economic_growth = pd.read_csv(GLOBALIS_FP + "economic_growth_over_the_past_10_years--by--geo--time.csv")
    hdi = pd.read_csv(GLOBALIS_FP + "hdi_human_development_index--by--geo--time.csv")
    sex_ratio = pd.read_csv(GLOBALIS_FP + "sex_ratio_all_age_groups--by--geo--time.csv")
    income_pp = pd.read_csv(GLOBALIS_FP + "income_per_person_long_series--by--geo--time.csv")

    # Clean the dataframes
    country_data = country_data[[
        "country", "income_groups", "main_religion_2008", "name", "world_4region", "world_6region"
    ]]

    # output["country_data"] = country_data
    output["labour_participation"] = labour_participation
    output["ppp_gdp_per_capita"] = ppp_gdp_per_capita
    output["democracy_score"] = democracy_score
    output["economic_growth"] = economic_growth
    output["hdi"] = hdi
    output["sex_ratio"] = sex_ratio
    output["income_pp"] = income_pp


    # Drop the rows from before 1950
    for key, value in output.items():
        value = value[value['time'] >= 1950]

    # Take the average of the rest
    labour_participation_mean = labour_participation.groupby('geo', as_index=False)['aged_15plus_labour_force_participation_rate_percent'].mean()
    ppp_gdp_per_capita_mean = ppp_gdp_per_capita.groupby('geo', as_index=False)['alternative_gdp_per_capita_ppp_wb'].mean()
    democracy_score_mean = democracy_score.groupby('geo', as_index=False)['democracy_score_use_as_color'].mean()
    economic_growth_mean = economic_growth.groupby('geo', as_index=False)['economic_growth_over_the_past_10_years'].mean()
    hdi_mean = hdi.groupby('geo', as_index=False)['hdi_human_development_index'].mean()
    sex_ratio_mean = sex_ratio.groupby('geo', as_index=False)['sex_ratio_all_age_groups'].mean()
    income_pp_mean = income_pp.groupby('geo', as_index=False)['income_per_person_long_series'].mean()

    # Merge into master dataframe
    master = pd.merge(country_data, labour_participation_mean, how="left", left_on="country", right_on="geo").drop(columns="geo")
    master = pd.merge(master, ppp_gdp_per_capita_mean, how="left", left_on="country", right_on="geo").drop(columns="geo")
    master = pd.merge(master, democracy_score_mean, how="left", left_on="country", right_on="geo").drop(columns="geo")
    master = pd.merge(master, economic_growth_mean, how="left", left_on="country", right_on="geo").drop(columns="geo")
    master = pd.merge(master, hdi_mean, how="left", left_on="country", right_on="geo").drop(columns="geo")
    master = pd.merge(master, sex_ratio_mean, how="left", left_on="country", right_on="geo").drop(columns="geo")
    master = pd.merge(master, income_pp_mean, how="left", left_on="country", right_on="geo").drop(columns="geo")
    output["master"] = master

    return output


"""


population_total_percent DIFFERENT FP

(data_quality_income_per_person)

"""

if __name__ == "__main__":
    setup_dfs()