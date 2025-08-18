import pandas as pd
import matplotlib.pyplot as plt
from ISLP import load_data

BASE_PATH = "../data/"
COLLEGE_DATA = "college.csv"
AUTO_DATA = "auto.csv"


def read_csv(path):
    try:
        return pd.read_csv(path, na_values=["?"])
    except Exception as e:
        print("Problem reading csv {}", e)


# print("Reading in CSV...")
colleges = read_csv(BASE_PATH + COLLEGE_DATA)
college3 = colleges.rename({"Unnamed: 0": "College"}, axis=1)
college3 = college3.set_index("College")
college = college3
#

# pd.plotting.scatter_matrix(college[[
# 'Top10perc', 'Apps', 'Enroll']], figsize=(8, 8)) # Top10perc : New students from top 10 % of high school class
# plt.suptitle("College Stats")
# plt.savefig('../plots/my_plot.png')

## 8e
pd.plotting.boxplot(college, column="Outstate", by="Private", figsize=(10, 8))
plt.suptitle("")
plt.xlabel("Private School")
plt.ylabel("Out of state tuition $")
plt.title("")
plt.savefig("../plots/OutstateVsPrivate.png")
summary_stats = college.groupby("Private")["Outstate"].describe()
# print(summary_stats)

# 8f
plt.figure()  # Clear old plot info
# help(pd.cut)
college["Elite"] = pd.cut(college["Top10perc"] / 100, [0, 0.5, 1], labels=["No", "Yes"])
# print("Count of elite universities: {}", pd.Series(college['Elite']).value_counts())
pd.plotting.boxplot(college, column="Outstate", by="Elite", figsize=(10, 8))
plt.suptitle("")
plt.xlabel("Elite School")
plt.ylabel("Out of state tuition $")
plt.title("")
plt.savefig("../plots/OutstateVsElite.png")

# 8g
plt.figure()  # Clear old plot info
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle(f"Application data for {len(college)} colleges")
axs[0, 1].set_title("Accept")
axs[1, 0].set_title("Enroll")
axs[1, 1].set_title("Top10perc")

college["Apps"].plot.hist(ax=axs[0, 0], bins=20, color="grey", edgecolor="black")
axs[0, 0].set_title("Applications received per college")
axs[0, 0].set_xlabel("Apps Received")
axs[0, 0].set_ylabel("Count of colleges")
college["Accept"].plot.hist(ax=axs[0, 1], bins=20, color="skyblue", edgecolor="black")
college["Enroll"].plot.hist(ax=axs[1, 0], bins=20, color="green", edgecolor="black")
college["Top10perc"].plot.hist(ax=axs[1, 1], bins=20, color="yellow", edgecolor="black")
axs[1, 1].set_ylabel("Count of colleges")
axs[1, 1].set_xlabel("Percentage of enrolled students from top 10% of class")
plt.tight_layout()
plt.savefig("../plots/CollegeHist.png")

plt.close()

## 8f

# ~500 colleges receive ~2500 apps
# ~420 colleges accept ~1250 apps (50% acceptance rate)
# ~310 colleges enroll ~333 apps

# Summary of above:
# The most frequent scenario is a college
# receives about 2500 apps, they accept about half of them,
# but only about a quarter of those accepted enroll.


# What does the 'Top10perc' histogram suggest
# about the academic profile of incoming students
# for the majority of these colleges?

# Answer:
# Of those that enroll
# The most frequent scenario is about 25% of those students
# are from the top of their class
# 25% of 333 ~88 students
# The most frequent scenario is a college enrolls ~88 students who were in the top 10% of their class
plt.figure()
autos_df = read_csv(BASE_PATH + AUTO_DATA)
print("Shape: {}".format(autos_df.shape))
print("Descriptive stats:")
print(autos_df.describe())

# 9a
print(
    "The qualitative predictors are name and origin. The rest of the predictors are all quantitative, e.g. mpg"
)

# 9b
print("Here is the range of each quantitative variable: ")
autos_df_without_origin = autos_df.drop("origin", axis=1)
print(
    autos_df_without_origin.max(numeric_only=True)
    - autos_df_without_origin.min(numeric_only=True)
)

# 9c
print("Here are the mean and standard deviation of each quantitative predictor")
print(autos_df_without_origin.mean(numeric_only=True))
print(autos_df_without_origin.std(numeric_only=True))


autos_df_without_origin["displacement"].hist(bins=50)
plt.savefig("../plots/DisplacementData.png")


# 9d

# Remove the 10th through the 85th observations
print(
    "Here are the range mean and standard deviation of each quantitative predictor with the 10th through 85th observations removed"
)

auto_df_without_origin_dropped = autos_df_without_origin.drop(
    autos_df_without_origin.index[10:85]
)

print("range------")
print(
    auto_df_without_origin_dropped.max(numeric_only=True)
    - auto_df_without_origin_dropped.min(numeric_only=True)
)

print("mean------")
print(auto_df_without_origin_dropped.mean(numeric_only=True))

print("standard deviation------")
print(auto_df_without_origin_dropped.std(numeric_only=True))

# 9e

# Plot cylinders vs weight
# Question is: does having lower cylinders generally mean having lower weight?
plt.close("all")

# What do I want to see?
# x-axis: the weight of the car
# y-axis: how many cylinders
# It sounds like I need a scatter plot

plt.suptitle("Cylinders by Weight")
pd.plotting.scatter_matrix(autos_df[["cylinders", "weight"]], figsize=(10, 6))


plt.savefig("../plots/WeightVsCyl.png")

# As expected, we see that increasing the cylinders in a car generally leads to an increase in weight

# Now explore something that I would not make assumptions about

plt.close("all")

plt.suptitle("Displacement by Acceleration")
pd.plotting.scatter_matrix(autos_df[["displacement", "acceleration"]], figsize=(10, 6))
plt.savefig("../plots/DisplVsAccel.png")

# Shows heteroscedasticity, e.g. acceleration becomes negatively linear with displacement after we exceed about 200 in displacement.


# 9f
plt.close("all")
plt.suptitle("MPG by Cylinders")
pd.plotting.scatter_matrix(autos_df[["mpg", "cylinders"]], figsize=(10, 6))
plt.savefig("../plots/MPGvsCyl.png")
# As expected, lower cylinders generally has higher MPG


# 10a

plt.close("all")
boston = load_data("Boston")

print("BOSTON DATA SET: ")
print(boston)
# https://intro-stat-learning.github.io/ISLP/datasets/Boston.html

# 10b
print(boston.shape)
# 506 rows, 13 columns
# The rows each represent a piece of sample data, an observation, in this case an observation is a suburb of boston
# The columns are the predictors contained in the observation

# 10c
# Let's make a scatter plot of pupil teacher ratio vs crime
# We are wondering: is there a relationship between pupil-teacher ratio and crime

pd.plotting.scatter_matrix(boston[["ptratio", "crim"]], figsize=(10, 6))
plt.savefig("../plots/PTRatioVsCrim.png")
plt.close("all")
# We see a spike in crime when pupil to teacher ratio is ~20

# Lets look at nitrous oxide concentration vs median value of homes in 1000s
# We are wondering: if an area has high nitrous oxide concentration, are the homes cheaper?
pd.plotting.scatter_matrix(boston[["nox", "medv"]], figsize=(10, 6))
plt.savefig("../plots/NoxVsMedv.png")
# Actually yes - once we reach a certain nitrous level, we see home levels stay below ~30. This suggests certain areas with these nitrous levels have less expensive homes
# The data is much more varied below this threshold nitrous level.

# 10d
# We saw a spike in crime rate for pupil to teacher ratio. but maybe there's a better predictor for this.
# Lets examine something like - age and crime rate
plt.close("all")
pd.plotting.scatter_matrix(boston[["age", "crim"]], figsize=(10, 6))
plt.savefig("../plots/AgeVsCrim.png")
# If we are looking at homes that are >80 years old, we see the crime rate rise to higher levels than previously seen. Old, old houses = high crime.

# 10e
# Pretend you shopping for a suburb and are concerned with high crime rates, tax rates, and pupil teacher ratios.

# Crime
plt.close("all")
boston["crim"].plot.hist()
plt.savefig("../plots/CrimBoston.png")
# There are some outliers for crime rates that are high, yes, a few of them. The range is high here.

plt.close("all")
boston["ptratio"].plot.hist()
plt.savefig("../plots/PTRatioBoston.png")
# The data here is more evenly disperesed... Range is lower

plt.close("all")
boston["tax"].plot.hist()
plt.savefig("../plots/TaxBoston.png")
# Range is pretty high here, from 200 to 700. The most frequent scenario is your suburb is taxed the max!


# 10f
plt.close("all")
status_counts = boston["chas"].value_counts()
print("Not near charles river vs near charles river: " + str(status_counts))
status_counts.plot(kind="bar", rot=0)  # rot=0 keeps labels horizontal
plt.savefig("../plots/CharlesRiverBoston.png")


# Overall stats:
print(boston.describe())
# Median PTratio is 19.050000

# 10h
plt.close("all")
boston["medv"].plot.hist()
plt.savefig("../plots/medv.png")

print("The min value of medv is " + str(boston["medv"].min()))

suburb_with_min_price = boston[boston["medv"] == boston["medv"].min()]

print("The total suburb info for this one(s) is \n" + str(suburb_with_min_price))

# Crim is near the max for one, and much higher than the median. It's in the upper range of crime.
# ZN is median
# There's a higher than average non-retail business acres, maybe industrial?
# chas - these are not close to the charles river,
# Noxious fumes are higher than median. In fact they are above the 75% percentile, more evidence for industrial
# These are the oldest homes on the list, the highest age ranking
# Overall we see a trend that undeseriable characteristics come in batches - we extremes in several predictors that negatively impact quality of life


# 10i
suburb_with_more_than_seven_rooms = boston[boston["rm"] > 7.00]
suburb_with_more_than_eight_rooms = boston[boston["rm"] > 8.00]


print("Those with greater than 7 rooms: \n" + str(suburb_with_more_than_seven_rooms))
print("Those with greater than 8 rooms: \n" + str(suburb_with_more_than_eight_rooms))

# A couple of homes are close to the river, which is unusual given the small selection
#
