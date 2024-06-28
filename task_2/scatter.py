import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Housing.csv")


# Graphique nuage de point
plt.figure(figsize=(8, 6))
plt.scatter(df['area'], df['price'], alpha=0.4, c='purple')
plt.title('Relationship between area and price')
plt.xlabel('Area (square feet)')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()