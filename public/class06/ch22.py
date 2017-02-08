# ch22.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#outliers

# By default, BoxPlot charts show outliers above and below the
# whiskers. However, the display of outliers can be turned on or off
# with the outliers parameter:

from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = BoxPlot(df, values='mpg', label='cyl', outliers=False,
            title="MPG Summary (grouped by CYL, no outliers)")

output_file("boxplot.html")

show(p)


