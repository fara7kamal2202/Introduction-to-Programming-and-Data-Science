#https://www.best-selling-cars.com/germany/2024-full-year-germany-best-selling-electric-cars-by-brand-and-model/
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
german_market = [3435778, 3607258, 2917678, 2622132, 2651357, 2844609, 2817331]
german_market_bev = [36062, 63281, 194163, 355961, 	470559, 524219, 380609]



fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(x=years, height=german_market, width=0.7,align='center')
ax.bar(x=years, height=german_market_bev, width=0.7,  align='center')

plt.xticks(years)
plt.legend(['Total German Car Market', 'All Electric Cars Sold'])

plt.tight_layout()
plt.show()