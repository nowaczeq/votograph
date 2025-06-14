# Setup dataframes from GapMinder datasets
import numpy as np
import pandas as pd


def setup_dfs():
    output = {}

    GLOBALIS_FP = "ddf--gapminder--systema_globalis\\countries-etc-datapoints\\ddf--datapoints--"

    # Load the datasets
    country_data = pd.read_csv("ddf--gapminder--systema_globalis\\ddf--entities--geo--country.csv")
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
    master = pd.merge(country_data, labour_participation, how="left", left_on="country", right_on="geo")
    master = pd.merge(master, ppp_gdp_per_capita, how="left", left_on="country", right_on="geo")
    master = pd.merge(master, democracy_score, how="left", left_on="country", right_on="geo")

    # DO NOT TURN THIS ON IT WILL SHUT DOWN THE COMPUTER BRO
    # Change this to averages
    # master = pd.merge(master, economic_growth, how="left", left_on="country", right_on="geo")
    # master = pd.merge(master, hdi, how="left", left_on="country", right_on="geo")
    # master = pd.merge(master, sex_ratio, how="left", left_on="country", right_on="geo")
    # master = pd.merge(master, income_pp, how="left", left_on="country", right_on="geo")

    print(master.head(5))
    return output


"""


population_total_percent DIFFERENT FP

(data_quality_income_per_person)

"""

if __name__ == "__main__":
    setup_dfs()