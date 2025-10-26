#https://caredge.com/guides/electric-vehicle-market-share-and-sales
import matplotlib.pyplot as plt
import pandas as pd

bev_percentage = {'Q1 2023': 7.3,
                  'Q2 2023': 7.2,
                  'Q3 2023': 7.9,
                  'Q4 2023': 8.1,
                  'Q1 2024': 7.3,
                  'Q2 2024': 8.0,
                  'Q3 2024': 8.9,
                  'Q4 2024': 8.7,
                  'Q1 2025': 7.5,
                  'Q2 2025': 7.4}


df = pd.DataFrame(list(bev_percentage.items()), columns=['Quarter', 'BEV Percentage'])

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Quarter'], df['BEV Percentage'], color='dodgerblue', s=80, edgecolors='black')
plt.plot(df['Quarter'], df['BEV Percentage'], color='lightgray', linestyle='--', linewidth=1)  # optional trend line
plt.title('US EV Car Sale Percentage 2023-2025', fontsize=14, fontweight='bold')
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='solid', alpha=0.6)
plt.tight_layout()
plt.show()

print(df)