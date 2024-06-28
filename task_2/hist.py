import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Housing.csv")

# Histogramme de la colonne 'bedrooms'
plt.figure(figsize=(10, 4))
plt.hist(df['bedrooms'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of bedrooms')
plt.xlabel('beedroom')
plt.ylabel('Fréquence')
plt.grid(True)
plt.show()