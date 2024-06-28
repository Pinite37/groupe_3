# Chargement des packages
library(readr)
library(ggplot2)

# Chargement du dataset Housing.csv
data <- read_csv("Housing.csv")
View(data)


# l'histogramme pour 'bedrooms'
histogram <- ggplot(data, aes(x = bedrooms)) +
  geom_histogram(binwidth = 1, fill = "blue", color = "black") +
  labs(title = "Distribution du Nombre de Chambres",
       x = "Nombre de Chambres",
       y = "Fréquence")

print(histogram)