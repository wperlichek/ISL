import pandas as pd
import matplotlib.pyplot as plt

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
autos = read_csv(BASE_PATH + AUTO_DATA)
print("Shape: {}".format(autos.shape))
print("Descriptive stats:")
print(autos.describe())

# 9a
print(
    "The qualitative predictors are name and origin. The rest of the predictors are all quantiative, e.g. mpg"
)

print("Here is the range of each quantitative variable: ")
for ele in autos.describe():
    print(ele)
