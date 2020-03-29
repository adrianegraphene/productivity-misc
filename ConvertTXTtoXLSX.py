import pandas as pd

#read txt file and give a header column name (lets you play with string functions)
file = pd.read_csv('ListCopiedFromDiscord.txt', sep = '\t', names=["Projects"])

#Remove all numbers, periods, and spaces on left side
file = file['Projects'].str.lstrip('1234567890. ')

file.to_excel('ListCopiedFromDiscord.xlsx', 'Sheet 1')