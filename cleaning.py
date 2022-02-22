from tempfile import tempdir
import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df['Luminosity']

print(df.shape)

df = df.rename({'1': "Mass"}, axis='columns')

df.to_csv("cleaned.csv")