# Setup dataframes from GapMinder datasets
import numpy as np
import pandas as pd


def setup_dfs():
    output = {}

    GLOBALIS_FP = "ddf--gapminder--systema_globalis\\countries-etc-datapoints\\ddf--datapoints--"

    country_data = pd.read_csv("ddf--gapminder--systema_globalis\\ddf--entities--geo--country.csv")
    labour_participation = pd.read_csv(GLOBALIS_FP + "income_per_person_with_projections--by--geo--time.csv")
    ppp_gdp_per_capita = pd.read_csv(GLOBALIS_FP + "alternative_gdp_per_capita_ppp_wb--by--geo--time.csv")
    democracy_score = pd.read_csv(GLOBALIS_FP + "democracy_score_use_as_color--by--geo--time.csv")
    economic_growth = pd.read_csv(GLOBALIS_FP + "economic_growth_over_the_past_10_years--by--geo--time.csv")
    hdi = pd.read_csv(GLOBALIS_FP + "hdi_human_development_index--by--geo--time.csv")
    sex_ratio = pd.read_csv(GLOBALIS_FP + "sex_ratio_all_age_groups--by--geo--time.csv")
    income_pp = pd.read_csv(GLOBALIS_FP + "income_per_person_long_series--by--geo--time.csv")




    return output


"""


population_total_percent DIFFERENT FP

(data_quality_income_per_person)

"""

setup_dfs()