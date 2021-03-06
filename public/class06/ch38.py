# ch38.py

# ref
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#tooltips

# The tooltips parameter can be used to add information to the hover
# tool and is supported for the scatter and line charts. The format is
# the same as the tooltips attribute of the hover tool.

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

tooltips=[
    ('Cylinders', '@cyl'),
    ('Displacement', '@displ'),
    ('Weight', '@weight'),
    ('Acceleration', '@accel')
]

p = Scatter(df, x='mpg', y='hp', title="HP vs MPG",
            xlabel="Miles Per Gallon", ylabel="Horsepower",
            tooltips=tooltips)

output_file("/tmp/ch38.html")

show(p)


