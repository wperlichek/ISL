import pandas as pd

BASE_PATH = "../data/"
COLLEGE_DATA = "college.csv"

def read_csv(path):
    try:
        return pd.read_csv(path)
    except:
        print("Problem reading csv")

print("Reading in CSV...")
csv_file = read_csv(BASE_PATH + COLLEGE_DATA)
print(csv_file)