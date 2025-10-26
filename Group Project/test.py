import pandas as pd
import matplotlib.pyplot as plt


auto_maker = pd.read_csv("largest_automakers.csv")
auto_maker_by_country = auto_maker[auto_maker['country'].isin(["China", "Germany", "United States"])]
auto_maker_by_country.drop(columns=['Symbol'], axis=1, inplace=True)
top_10_car_brands = auto_maker_by_country.head(10)
print(top_10_car_brands)

#     Rank            Name      marketcap  price (USD)        country
# 0      1           Tesla  1430812360704     430.3000  United States
# 2      3          Xiaomi   176943726592       6.8000          China
# 3      4             BYD   136956219874      15.5309          China
# 5      6   Mercedes-Benz    59525358406      61.8186        Germany
# 6      7             BMW    56813452077      93.2034        Germany
# 8      9      Volkswagen    53621189759     106.1240        Germany
# 9     10  General Motors    53621022720      56.3200  United States
# 11    12            Ford    46066880512      11.5750  United States
# 12    13         Porsche    43922833984      48.2139        Germany
# 15    16     Seres Group    36698154951      22.4678          China

total_market_cap = auto_maker['marketcap'].sum()
market_cap = auto_maker.groupby('country').marketcap.sum()
market_cap.sort_values(ascending=False, inplace=True)

print(market_cap)

market_cap_us = market_cap['United States'] / total_market_cap * 100
market_cap_china = market_cap['China'] / total_market_cap * 100
market_cap_germany = market_cap['Germany'] / total_market_cap * 100
market_cap_other = 100 - (market_cap_us + market_cap_china + market_cap_germany)


pie_chart_labels = 'Germany', 'United States', 'China', 'Rest of the World'
value = market_cap_germany, market_cap_us, market_cap_china, market_cap_other

print(value)

plt.pie(value, labels=pie_chart_labels, autopct='%1.1f%%')
plt.title('Germany, United States, China, Rest of the World Car Sale Market Capital')
plt.show()