# sb16.py

# Ref:
# https://seaborn.pydata.org/tutorial/aesthetics.html#overriding-elements-of-the-seaborn-styles

import seaborn as sns

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

print(sns.axes_style())

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sns.set_style("darkgrid", {"axes.facecolor": ".9", 'grid.color': 'red'})
sinplot()
plt.show()
