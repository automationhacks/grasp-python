# Pycharm supports data science related plots in scientific mode (pro feature)

# https://www.jetbrains.com/help/pycharm/matplotlib-support.html#
# However you can install ipython module
# And run these code snippets in Python console

# Reference for these examples:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.line.html

import pandas as pd

# Base data via pandas Series
s = pd.Series([2, 5, 10])

# Plot a line
s.plot.line()

# Base data via pandas data frame
df = pd.DataFrame({
    'pig': [20, 18, 489, 675, 1776],
    'horse': [4, 25, 281, 600, 1900]
}, index=[1990, 1997, 2003, 2009, 2014])


# Population of animals (pig, horse) over the years
lines = df.plot.line()

# Subplots example, array of axes is returned
axes = df.plot.line(subplots=True)

# Relationship between both populations
lines = df.plot.line(x='pig', y='horse')

# Pie chart
plot = df.plot.pie(y='horse', figsize=(5, 5))