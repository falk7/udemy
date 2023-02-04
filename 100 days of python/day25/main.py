# import csv 


# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for index, row in enumerate(data):
#         if index > 0:
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data[data.temp == data.temp.max()])
# print(sum(data_list) / len(data_list))
monday = data[data.day == "Monday"]
print(monday.temp * 9 / 5 +32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# "Primary Fur Color"
data["Primary Fur Color"].value_counts().to_csv("squirrel_colors.csv")