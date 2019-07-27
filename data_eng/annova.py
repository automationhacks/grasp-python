"""
https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/hypothesis-testing/anova/
"""

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv('/Users/gaurav/Downloads/PlantGrowth.csv')
data.boxplot('weight', by='group')

mod = ols('weight ~ group', data=data).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)

print(aov_table)
