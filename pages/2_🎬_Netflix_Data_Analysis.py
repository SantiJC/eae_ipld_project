# The libraries you have to use
import pandas as pd
import matplotlib.pyplot as plt

# Some extra libraries to build the webapp
import streamlit as st


# ----- Page configs -----
st.set_page_config(
    page_title="Santi's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write("Interactive Project to load a dataset with information about Netflix Movies and Series, extract some insights usign Pandas and displaying them with Matplotlib.")
    st.write("Data extracted from: https://www.kaggle.com/datasets/shivamb/netflix-shows (with some cleaning and modifications)")


# ----- Title of the page -----
st.title("🎬 Netflix Data Analysis")
st.divider()


# ----- Loading the dataset -----

@st.cache_data
def load_data():
    data_path = "data/netflix_titles.csv"

    movies_df = pd.read_csv(data_path, index_col="show_id")  # TODO: Ex 2.1: Load the dataset using Pandas, use the data_path variable and set the index column to "show_id"

    return movies_df   # a Pandas DataFrame


movies_df = load_data()

# Displaying the dataset in a expandable table
with st.expander("Check the complete dataset:"):
    st.dataframe(movies_df)


# ----- Extracting some basic information from the dataset -----

# TODO: Ex 2.2: What is the min and max release years?
min_year = min(movies_df["release_year"])
max_year = max(movies_df["release_year"])

# TODO: Ex 2.3: How many director names are missing values (NaN)?
num_missing_directors = len(movies_df[movies_df["director"].isnull()==True])

# TODO: Ex 2.4: How many different countries are there in the data?
for country, index in zip(movies_df["country"].isnull(), range(len(movies_df))):
    if country == True:
        movies_df["country"][index] = "Unknown"

countries = []
for country in movies_df["country"]:
    country = str(country).split(",")
    for x in country:
        x = x.strip()
        countries.append(x)

countries=set(countries)
final_countries = []

for x in countries:
    if len(x)>2 and x != "nan":
        final_countries.append(x)
n_countries = len(final_countries)

# TODO: Ex 2.5: How many characters long are on average the title names?
lengths = []
for title in movies_df["title"]:
    lengths.append(len(title))
avg_title_length = sum(lengths)/len(lengths)


# ----- Displaying the extracted information metrics -----

st.write("##")
st.header("Basic Information")

cols1 = st.columns(5)
cols1[0].metric("Min Release Year", min_year)
cols1[1].metric("Max Release Year", max_year)
cols1[2].metric("Missing Dir. Names", num_missing_directors)
cols1[3].metric("Countries", n_countries)
cols1[4].metric("Avg Title Length", str(round(avg_title_length, 2)) if avg_title_length is not None else None)


# ----- Pie Chart: Top year producer countries -----

st.write("##")
st.header("Top Year Producer Countries")

cols2 = st.columns(2)
year = cols2[0].number_input("Select a year:", min_year, max_year, 2005)

# TODO: Ex 2.6: For a given year, get the Pandas Series of how many movies and series 
# combined were made by every country, limit it to the top 10 countries.
records_2005 = movies_df.loc[movies_df["release_year"]==year]
top_10_countries = records_2005["country"].value_counts().head(10)

# print(top_10_countries)
if top_10_countries is not None:
    fig = plt.figure(figsize=(8, 8))
    plt.pie(top_10_countries, labels=top_10_countries.index, autopct="%.2f%%")
    plt.title(f"Top 10 Countries in {year}")

    st.pyplot(fig)

else:
    st.subheader("⚠️ You still need to develop the Ex 2.6.")


# ----- Line Chart: Avg duration of movies by year -----

st.write("##")
st.header("Avg Duration of Movies by Year")

# TODO: Ex 2.7: Make a line chart of the average duration of movies (not TV shows) in minutes for every year across all the years.
movies = movies_df.loc[movies_df["type"]=="Movie"]


movies_avg_duration_per_year = []  # TODO: movies_avg_duration_per_year has to be a Pandas Series with the average duration of movies per year
years = []
result = {}


for year in range(1925,2022):
    durations=[]
    for x in movies.loc[movies["release_year"]==year]["duration"]:
        durations.append(int(x.replace(" min","")))
    if len(durations) != 0:
        years.append(year)
        movies_avg_duration_per_year.append(sum(durations)/len(durations))
        
result = {"Years": years, "Avg_duration":movies_avg_duration_per_year}
avg_duration_df = pd.DataFrame(result) 


if movies_avg_duration_per_year is not None:
    fig = plt.figure(figsize=(9, 6))

    plt.plot(avg_duration_df["Years"],avg_duration_df["Avg_duration"])   # TODO: generate the line plot using plt.plot() and the information from movies_avg_duration_per_year (the vertical axes with the minutes value) and its index (the horizontal axes with the years)

    plt.title("Average Duration of Movies Across Years")

    st.pyplot(fig)

else:
    st.subheader("⚠️ You still need to develop the Ex 2.7.")

