# %% [markdown]
# # Seaborn Practice

# %% [markdown]
# ## Q1: Exercies data

# %%
# Import library
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Load dataset
exercises = pd.read_csv('C:/Users/13176/Desktop/2026 Classes/Information Infrastructure II/HW/HW08/Exercise_Data.csv')
print (exercises.head())

# %% [markdown]
# ### Create Heatmap

# %%
# Create a heatmap of the pulse data. Create a categorical plot fo pulse values by diet and by type of exercise.
pulse_only = exercises[['1 min', '15 min', '30 min']]
pulse_only.index = exercises['id']

sns.heatmap(pulse_only, annot=False, cmap='YlOrRd')
plt.title('Pulse Data Heatmap')
xlabel = ['1 min', '15 min', '30 min']
plt.xlabel('Time')
plt.ylabel('Participant ID')
plt.show()

# %% [markdown]
# ### Categorical plot

# %%
# Create Categorical plot for pulse values by diet and by type of exercise.
exercises_long = exercises.melt(
    id_vars=['id', 'diet', 'kind'], 
    value_vars=['1 min', '15 min', '30 min'], 
    var_name='time', 
    value_name='pulse'
)
# Melting into long format for categorical plotting
sns.catplot(x='time', y='pulse', hue='diet', col='kind', data=exercises_long, kind='box')
# Can add 'col_wrap = 1' tp catplot to make the plots vertical instead of horizontal to better visualize their diffrences/visuals.

xlabel = ['1 min', '15 min', '30 min']
plt.xlabel('Time')
plt.ylabel('Pulse')
plt.suptitle('Pulse Values by Diet and Exercise Type', y=1.02)


# %% [markdown]
# #### Conclusions: 
# * Resting heart rates are steady between 80-100 bpm (beats per minute). Walking slightly increases but still consistent. Finally running shows lots of dramatic changes with some outliners visually noticable, with pulses rates also being far higher than the previous catagories.
# 
# * The median when running creates an upward trend throught the long duration, creating higher median pulses rates.
# 
# * The 'No Fat' (Orange) consistantly results in higher median pulses than 'Low Fat' (blue). This is greatly noticable during Running.
# * Overall a review reguarding the outliners should be looked into to see if they skewer the running heavly.3 

# %% [markdown]
# ## Q2: Planets Dataset (Build-in Seaborn)

# %%
# Load planetsdataset
planets = sns.load_dataset('planets')
print(planets.head())

# %% [markdown]
# ### 1. Relational Plots-

# %%
# 1.1 Scatter Plot: Distance vs. Orbital Period (log scale)
sns.set_theme(style="whitegrid", context="talk") 
plt.figure(figsize=(12, 7))

sns.scatterplot(data=planets, x="distance", y="orbital_period", hue="method", alpha=0.7, edgecolor='w', linewidth=0.5)
plt.xscale('log')
plt.yscale('log')

# Placeing legend outside the plot area to avoid overlap with data points.
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title="Discovery Method")
sns.despine() # Remove top and right spines for a cleaner look

plt.title("Relational: Distance vs Orbital Period (Log Scale)")
plt.xlabel("Distance (log scale)")
plt.ylabel("Orbital Period (log scale)")
plt.tight_layout()
plt.show()

# %% [markdown]
# #### Interpretation
# - The scatter plot shows clear clustering by detection method, especially for Transit and Radial Velocity.
# - There is a positive relationship on the log-log scale: planets farther from their stars generally have longer orbital periods.

# %%
# 1.2 Line Plot: Year vs. Mean Orbital Period (cleaned for readability)
sns.set_theme(style="whitegrid", context="talk")

# Keep complete rows and focus on the most common discovery methods for a clearer trend view
line_data = planets.dropna(subset=["year", "orbital_period", "method"]).copy()
top_methods = line_data["method"].value_counts().head(6).index
line_data = line_data[line_data["method"].isin(top_methods)]

plt.figure(figsize=(12, 6))
ax = sns.lineplot(
    data=line_data,
    x="year",
    y="orbital_period",
    hue="method",
    estimator="mean",
    errorbar=None,
    linewidth=2.4,
    palette="tab10"
 )

ax.set_yscale("log")
ax.set_title("Relational: Year vs Mean Orbital Period", pad=12)
ax.set_xlabel("Year of Discovery")
ax.set_ylabel("Mean Orbital Period (log scale)")
ax.grid(alpha=0.25, which="both")
ax.legend(
    title="Discovery Method",
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    frameon=False
 )
sns.despine(offset=8, trim=True)
plt.tight_layout()
plt.show()
# Limited to top 6 methods for better readability and trend visualization.

# %% [markdown]
# #### Interpretation
# - The line plot suggests that methods are concentrated in different discovery periods.
# - Imaging and timing-based methods tend to have higher mean orbital-period values than Transit-based discoveries.

# %% [markdown]
# ### 2. Distributional Plots-

# %%
# 2.1 Histogram: Distribution of Planet Masses (cleaned for readability)
sns.set_theme(style="whitegrid", context="talk")

mass_data = planets["mass"].dropna() # Dropped missing values to focus on actual mass distribution and avoid skewing the histogram with NaNs.

plt.figure(figsize=(11, 6))
ax = sns.histplot(
    data=mass_data,
    bins=28,
    kde=True,
    color="#4C78A8",
    edgecolor="white",
    linewidth=0.6,
    alpha=0.85
)

ax.axvline(
    mass_data.median(),
    color="#E45756",
    linestyle="--",
    linewidth=2,
    label=f"Median = {mass_data.median():.2f}"
)

ax.set_title("Distribution of Planet Masses", pad=12)
ax.set_xlabel("Mass (Jupiter Masses)")
ax.set_ylabel("Count")
ax.grid(alpha=0.2)
ax.legend(frameon=False)
sns.despine(offset=8, trim=True)
plt.tight_layout()
plt.show()

# %% [markdown]
# #### Interpretation
# - The mass distribution is strongly right-skewed.
# - Most planets are concentrated at lower masses, with relatively few high-mass planets creating a long right tail.
# - Outliers on the right are expected within this dataset.

# %%
# 2.2 KDE Plot: Distribution of Distances by Detection Method (cleaned)
sns.set_theme(style="whitegrid", context="talk")

kde_data = planets.dropna(subset=["distance", "method"]).copy() # Dropped missing values to focus on actual distance distribution and method comparison without skewing from NaNs.
kde_data = kde_data[kde_data["distance"] > 0]

# Focus on the most represented methods to keep the chart readable
kde_top_methods = kde_data["method"].value_counts().head(5).index # limited to top 5 methods for better readability and trend visualization.
kde_data = kde_data[kde_data["method"].isin(kde_top_methods)]

plt.figure(figsize=(11, 6))
ax = sns.kdeplot(
    data=kde_data,
    x="distance",
    hue="method",
    fill=True,
    common_norm=False,
    alpha=0.25,
    linewidth=2,
    cut=0
)

ax.set_xscale("log")
ax.set_title("KDE: Distribution of Distances by Detection Method (Top 5)", pad=12)
ax.set_xlabel("Distance (log scale)")
ax.set_ylabel("Density")
ax.grid(alpha=0.2, which="both")
sns.despine(offset=8, trim=True)
plt.tight_layout()
plt.show()

# %% [markdown]
# #### Interpretation
# - Detection methods show different distance ranges.
# - Radial Velocity is more concentrated at closer distances, while Transit, Imaging, and timing-related methods are spread across broader ranges.

# %% [markdown]
# ### 3. Categorical Plots-

# %%
# 3.1 Box Plot: Orbital Period by Detection Method (cleaned)
sns.set_theme(style="whitegrid", context="talk")

cat_data = planets.dropna(subset=["method", "orbital_period"]).copy() # Removed outliners and missing values to focus on actual method comparison without skewing from NaNs or extreme values.

# Order methods by median orbital period for easier comparison
method_order = (
    cat_data.groupby("method")["orbital_period"]
    .median()
    .sort_values()
    .index
)

plt.figure(figsize=(12, 7))
ax = sns.boxplot(
    data=cat_data,
    y="method",
    x="orbital_period",
    order=method_order,
    color="#72B7B2",
    width=0.6,
    showfliers=False
)

ax.set_xscale("log")
ax.set_title("Box Plot: Orbital Period by Detection Method", pad=12)
ax.set_ylabel("Detection Method")
ax.set_xlabel("Orbital Period (log scale)")
ax.grid(axis="x", alpha=0.25, which="both")
sns.despine(offset=8, trim=True)
plt.tight_layout()
plt.show()

# %% [markdown]
# #### Interpretation
# - Orbital period differs substantially by detection method.
# - Imaging and timing-based methods generally identify planets with longer orbital periods, while Transit and Radial Velocity are centered lower.

# %%
# 3.2 Count Plot: Number of Planets Found by Year (cleaned)
sns.set_theme(style="whitegrid", context="talk")

year_counts = (
    planets["year"]
    .dropna()
    .astype(int)
    .value_counts()
    .sort_index()
)

count_data = year_counts.reset_index()
count_data.columns = ["year", "count"]

plt.figure(figsize=(12, 6))
ax = sns.barplot(
    data=count_data,
    x="year",
    y="count",
    color="#4C78A8",
    edgecolor="white",
    linewidth=0.4
)

# Reduce x-axis label density for readability
tick_positions = list(range(0, len(count_data), 3))
ax.set_xticks(tick_positions)
ax.set_xticklabels(count_data["year"].iloc[tick_positions], rotation=45, ha="right")

ax.set_title("Count of Planets Discovered by Year", pad=12)
ax.set_xlabel("Year of Discovery")
ax.set_ylabel("Number of Planets Discovered")
ax.grid(axis="y", alpha=0.25)
sns.despine(offset=8, trim=True)
plt.tight_layout()
plt.show()

# %% [markdown]
# #### Interpretation
# - Discoveries rise sharply after the mid-2000s and peak around 2011.
# - After the peak, yearly counts decline somewhat but remain much higher than in the earliest years.

# %% [markdown]
# ### Overall Highlights
# - The clearest graph is the discovery timeline, which shows a sharp increase in planet discoveries after about 2006 and a peak around 2011.
# - The strongest comparison graph is the orbital-period box plot, because it clearly shows how detection methods differ across a wide range of orbital periods.
# - Together, these two plots explain both when discoveries accelerated and how detection methods influence the type of planets observed.


