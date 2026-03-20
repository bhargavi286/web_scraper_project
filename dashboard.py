import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Web Scraper Dashboard", layout="wide")

st.title(" Web Scraper Dashboard with Analytics")

# Load data
df = pd.read_csv("data.csv")

st.subheader(" Scraped Data")
st.dataframe(df)

st.subheader(" Basic Info")
st.write("Total Rows:", len(df))
st.write("Columns:", list(df.columns))

# Search
if "Title" in df.columns:
    search = st.text_input("Search Title")

    if search:
        df = df[df["Title"].str.contains(search, case=False, na=False)]

st.subheader(" Title Length Analysis")

# create simple metric: length of title
df["Length"] = df["Title"].apply(len)

fig, ax = plt.subplots()
ax.hist(df["Length"])
ax.set_title("Distribution of Title Lengths")
ax.set_xlabel("Length")
ax.set_ylabel("Count")

st.pyplot(fig)