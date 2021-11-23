from pandas.core.algorithms import mode
import numpy as np
import pandas as pd
import pandasql as ps
from datetime import datetime
import matplotlib.pyplot as plt

# # midterm 1 log in data

# # log in 2011 data(a/b)
# print("[LOG: " + str(datetime.now()) + " - about to load 2011 CSV data]")
# df_midterm_2011b = pd.read_csv('2011B42B.csv',index_col='region_id')
# print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")

# # log in 2016 data(a/b)
# print("[LOG: " + str(datetime.now()) + " - about to load 2016 CSV data]")
# df_midterm_2016b = pd.read_csv('2016G43B.csv',index_col='POA_CODE_2016')
# print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")

# # log in 2016 maroubra data
# print("[LOG: " + str(datetime.now()) + " - about to load 2016 maroubra CSV data]")
# maroubra_2016 = pd.read_csv('df_maroubra_2016.csv')
# print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")

# # log in 2011 maroubra data
# print("[LOG: " + str(datetime.now()) + " - about to load 2011 maroubra CSV data]")
# maroubra_2011 = pd.read_csv('df_maroubra_2011.csv')
# print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")

# # Data Comparing
# data_2016b = pd.read_csv('df_maroubra_2016b.csv',usecols=[1])
# # data_2016b.to_csv("2016datab.csv")
# print(data_2016b)
# data_2016b.to_csv('df_maroubra_2011b.csv',mode='a') # Add 2016 data to 2011 data to compare
# # Then change the file name to ("compare2011_2016")




# midterm 2 - data headings_2011
# print("[LOG: " + str(datetime.now()) + " - about to run demo 2]")
# df_columnsName = pd.DataFrame(df_midterm_2011.columns.values.tolist(), columns=['Property'])
# df_columnsName.to_csv("df_columnsName_2011.csv")
# print("[LOG: " + str(datetime.now()) + " - finished demo 2]")

# # midterm 2 - data headings_2016
# print("[LOG: " + str(datetime.now()) + " - about to run data 2]")
# df_columnsNameB = pd.DataFrame(df_midterm_2016b.columns.values.tolist(), columns=['Property'])
# df_columnsNameB.to_csv("df_columnsNameB.csv")
# print("[LOG: " + str(datetime.now()) + " - finished data 2]")

# # midterm 3 - select specific rigion data
# print("[LOG: " + str(datetime.now()) + " - about to run midterm 3]")
# df_maroubra_2016b = df_midterm_2016b.loc['POA2035']
# # print(df_maroubra_2011b)
# df_maroubra_2016b.to_csv("df_maroubra_2016b.csv")
# print("[LOG: " + str(datetime.now()) + " - finished midterm 3]")


# midterm 4 conbine data(a) and data(b)
# log in compare data(a)
# print("[LOG: " + str(datetime.now()) + " - about to load compare_a CSV data]")
# df_compare_a = pd.read_csv('Compare2011_2016a.csv')
# print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")

# log in compare data(b)
# print("[LOG: " + str(datetime.now()) + " - about to load compare_b CSV data]")
# df_compare_b = pd.read_csv('Compare2011_2016b.csv')
# print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")
# print(df_compare_a)
# print(df_compare_b)
# df_compare_b.to_csv('Compare2011_2016a.csv',mode='a') # combine data
# print(df_compare_a)




# # midterm 5 Using matplotlib to create diagram for comparing

# extract total compared data
# df_total = df_compare_a[df_compare_a['Properties'].str.endswith('Tot')]
# print(df_total)
# df_total.to_csv("df_total.csv")

# # log in total compared data
print("[LOG: " + str(datetime.now()) + " - about to load Total compared CSV data]")
df_compared_total = pd.read_csv('df_total.csv',index_col=0)
print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")

# # Create total compared data picture
# df_compared_total.plot.bar(title = "Total compare between 2011 and 2016")
# plt.savefig("Total compare between 2011 and 2016.png")

# # create total male versus female data picture
df_compared_m = df_compared_total.loc["M_Tot_Tot"]
df_compared_fm = df_compared_total.loc["F_Tot_Tot"]
print(df_compared_m)
print(df_compared_fm)
plt.plot(df_compared_m,label = "male")
plt.plot(df_compared_fm, label = "female")
plt.legend()
plt.savefig("male versus female.png")

# # # create total compared male and female employed data picture
# df_compared_m = df_compared_total.loc["M_Emp_wkd_Tot_Tot"]
# df_compared_fm = df_compared_total.loc["F_Emp_wkd_Tot_Tot"]
# print(df_compared_m)
# print(df_compared_fm)
# plt.plot(df_compared_m,label = "male")
# plt.plot(df_compared_fm, label = "female")
# plt.legend()
# plt.savefig("male_Emp_compare_female.png")

# # # create total compared male and female unemployed data picture
# df_compared_m = df_compared_total.loc["M_Unem_look_Tot_Tot"]
# df_compared_fm = df_compared_total.loc["F_Unem_look_Tot_Tot"]
# print(df_compared_m)
# print(df_compared_fm)
# plt.plot(df_compared_m,label = "male")
# plt.plot(df_compared_fm, label = "female")
# plt.legend()
# plt.savefig("male_Unem_compare_female.png")

# # # create total compared male and female in labour force data picture
# df_compared_m = df_compared_total.loc["M_Tot_LF_Tot"]
# df_compared_fm = df_compared_total.loc["F_Tot_LF_Tot"]
# print(df_compared_m)
# print(df_compared_fm)
# plt.plot(df_compared_m,label = "male")
# plt.plot(df_compared_fm, label = "female")
# plt.legend()
# plt.savefig("male_LF_compare_female.png")

# # # create total compared male and female not in labour force data picture
# df_compared_m = df_compared_total.loc["M_Not_in_LF_Tot"]
# df_compared_fm = df_compared_total.loc["F_Not_in_LF_Tot"]
# print(df_compared_m)
# print(df_compared_fm)
# plt.plot(df_compared_m,label = "male")
# plt.plot(df_compared_fm, label = "female")
# plt.legend()
# plt.savefig("male_Not_in_LF_compare_female.png")



