import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("countries_data.csv")

# Convert population to numeric
df["Population"] = pd.to_numeric(df["Population"], errors="coerce")

# Sort by population
df = df.sort_values(by="Population", ascending=False)

# Plot top 10 populated countries
plt.figure(figsize=(10, 6))
plt.bar(df["Country"].head(10), df["Population"].head(10))
plt.xticks(rotation=45)
plt.title("Top 10 Most Populated Countries")
plt.xlabel("Country")
plt.ylabel("Population")
plt.tight_layout()
plt.show()
