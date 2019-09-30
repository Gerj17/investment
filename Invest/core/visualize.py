# TODO gather the data from the CSV  file, EC-Share Index.csv

import pandas as pd

df = pd.read_csv("EC-Share Index.csv", skiprows=1)

print(df)

