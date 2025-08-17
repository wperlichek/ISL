import pandas as pd
import matplotlib.pyplot as plt

BASE_PATH = "../data/"
COLLEGE_DATA = "college.csv"


def read_csv(path):
    try:
        return pd.read_csv(path)
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
axs[0, 0].set_title("Apps")
axs[1, 1].set_title("Enroll")

college["Apps"].plot.hist(ax=axs[0, 0], bins=20, color="skyblue", edgecolor="black")
college["Enroll"].plot.hist(ax=axs[1, 1], bins=20, color="purple", edgecolor="black")
plt.savefig("../plots/CollegeHist.png")

plt.close()
