# Chargement des packages
library(readr)
library(ggplot2)

# Chargement du dataset Housing.csv
data <- read_csv("Housing.csv")
View(data)



# graphique de dispersion pour 'area' vs 'price'
scatter_plot <- ggplot(data, aes(x = area, y = price)) +
  geom_point(color = "red") +
  labs(title = "Graphique de Dispersion : Superficie vs Prix",
       x = "Superficie (area)",
       y = "Prix (price)")

print(scatter_plot)

