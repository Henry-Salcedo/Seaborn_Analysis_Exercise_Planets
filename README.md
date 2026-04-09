# Seaborn_Analysis_Exercise/Planets

## Puropse
  Creating several visual with a main focus on Seaborn to analyis the diffrent datasets.

This project's aim was to focus on “Seaborn” to create stunning visuals.

The project reads both the 'Exercises.csv', and the 'Planet' dataset in Seaborn that is within “Scikit learn” that contains multiple columns.

The goal is to generate several visual plots, determine conclusions that can be made first with the exercise dataset, then with Planets determine which graphs of the 6 made the best demonstration on something notable about the data, and how its illustrated.
  
Key analyses include:
- Imported the required libraries: Seaborn, Pandas, and Matplotlib.
- Loaded the Exercise dataset from a CSV file.
- Created a heatmap of pulse values at different exercise times.
- Transformed the dataset into long format using melt() for categorical plotting.
- Generated a categorical plot comparing pulse values by diet and exercise type.
- Loaded the Seaborn built-in planets dataset.
- Created multiple visualizations including scatter plots, line plots, histograms, KDE plots, box plots, and count plots.
- Wrote short interpretations describing trends and patterns observed in each visualization.

## Class Design
The project can be classified into 5 different areas:

- Importing and loading datasets
- Data transformation and preparation
- Creating relational plots
- Creating distribution plots
- Creating categorical plots and interpreting results

## Class Attributes and Methods

### Data Loading

**Attributes:**

- exercises – DataFrame containing the exercise dataset
- planets – DataFrame containing the Seaborn planets dataset

**Methods:**

- pd.read_csv() – Loads the exercise dataset from a CSV file
- sns.load_dataset('planets') – Loads the planets dataset from Seaborn

---
### Data Preparation

**Attributes:**

- pulse_only – Subset containing pulse measurements
- exercises_long – Reshaped dataset used for categorical plots

**Methods:**

- .melt() – Converts wide format data into long format for plotting
- .dropna() – Removes missing values before creating graphs
- .copy() – Creates a safe copy of filtered datasets

---
### Relational Plots

**Attributes:**

planets dataset variables such as distance, orbital_period, and method

**Methods:**

sns.scatterplot() – Creates scatter plot comparing distance and orbital period
sns.lineplot() – Creates line plot showing trends in orbital period over time

---
### Distribution Plots

**Attributes:**

- mass_data – Planet mass values used for histogram
- kde_data – Dataset used to compare distance distributions by detection method

**Methods:**

- sns.histplot() – Creates histogram for planet mass distribution
- sns.kdeplot() – Creates kernel density estimate plot for distance distribution

---
### Categorical Plots

**Attributes:**

- cat_data – Dataset containing method and orbital period for categorical analysis
- year_counts – Counts of planets discovered per year

**Methods:**

- sns.heatmap() – Displays pulse values across time intervals
- sns.catplot() – Compares pulse values by diet and exercise type
- sns.boxplot() – Shows orbital period differences by detection method
- sns.countplot() – Displays number of planets discovered each year

---
### Results and Interpretaion

**Attributes:**
- Observed trends in pulse changes across exercises
- Differences in planet discovery methods and orbital periods
- Distribution patterns in planet mass and distances

**Methods:**
- plt.figure() – Creates plot figure size and layout
- sns.set_theme() – Applies styling to visualizations
- plt.show() – Displays plots for interpretation

---
## Limitations-
- I limited myself to what I learn in a class related to the project (e.g., not performing any scaled features or cross-validation).
- With an main focus in Seaborn I did my best to avoid relying to much on matplot, and uses Seaborn when I can.

## Final Thoughts / Conclusions-
These are my final conclusion reguarding each section:

Exercises Dataset:
- Resting heart rates are steady between 80-100 bpm (beats per minute). Walking slightly increases but still consistent. Finally running shows lots of dramatic changes with some outliners visually noticable, with pulses rates also being far higher than the previous catagories.

- The median when running creates an upward trend throught the long duration, creating higher median pulses rates.

- The 'No Fat' (Orange) consistantly results in higher median pulses than 'Low Fat' (blue). This is greatly noticable during Running.
- Overall a review reguarding the outliners should be looked into to see if they skewer the running heavly.
  
  Planet Dataset:
- The clearest graph is the discovery timeline, which shows a sharp increase in planet discoveries after about 2006 and a peak around 2011.
  
- The strongest comparison graph is the orbital-period box plot, because it clearly shows how detection methods differ across a wide range of orbital periods.
  
- Together, these two plots explain both when discoveries accelerated and how detection methods influence the type of planets observed.
