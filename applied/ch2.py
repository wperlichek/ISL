import pandas as pd
import matplotlib.pyplot as plt

BASE_PATH = "../data/"
COLLEGE_DATA = "college.csv"

def read_csv(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        print("Problem reading csv {}", e)

print("Reading in CSV...")
colleges = read_csv(BASE_PATH + COLLEGE_DATA)
college3 = colleges.rename({'Unnamed: 0': 'College'},axis=1)
college3 = college3.set_index("College")
college = college3
#

# pd.plotting.scatter_matrix(college[[
# 'Top10perc', 'Apps', 'Enroll']], figsize=(8, 8)) # Top10perc : New students from top 10 % of high school class
# plt.suptitle("College Stats")
# plt.savefig('../plots/my_plot.png')

## 8e

pd.plotting.boxplot(college, column='Outstate', by='Private', figsize=(10,8))
plt.suptitle('')
plt.xlabel('Private School')
plt.ylabel("Out of state tuition $")
plt.title('')
plt.savefig('../plots/my_plot2.png')
summary_stats = college.groupby('Private')['Outstate'].describe()
print(summary_stats)
plt.close()



