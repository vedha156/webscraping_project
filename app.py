import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("countries_data.csv")

# Convert Population to numeric
df["Population"] = pd.to_numeric(df["Population"], errors="coerce")

st.title("Countries Dashboard")

# Show Data Table
st.subheader("Scraped Data Table")
st.dataframe(df)

# Slider to choose number of countries
num_countries = st.slider(
    "Select number of top countries to display in bar chart:",
    min_value=5,
    max_value=len(df),
    value=10,
    step=1
)

# Sort dataframe by population descending
df_sorted = df.sort_values(by="Population", ascending=False).head(num_countries)

# Plot bar chart
st.subheader(f"Top {num_countries} Most Populated Countries")
fig, ax = plt.subplots(figsize=(15, 7))
ax.bar(df_sorted["Country"], df_sorted["Population"], color="skyblue")
plt.xticks(rotation=90)
plt.ylabel("Population")
plt.xlabel("Country")
plt.title(f"Top {num_countries} Countries by Population")
st.pyplot(fig)
