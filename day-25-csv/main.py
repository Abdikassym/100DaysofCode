# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] == "temp":
# #             pass
# #         else:
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # # Calculating mean
# # temp_list = data["temp"].to_list()
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
# #
# # # Or I can use pandas.series.mean()
# # print(data["temp"].mean())
# #
# # # Getting maximum by using series methods
# # print(data["temp"].max())
# #
# #
# # # Get data in columns -- Different methods to do the same task
# # print(data["condition"])
# # print(data.condition)
# #
# #
# # # Get data in a rows
# # print(data[data.day == "Monday"])  # return a row > 1. data file (data) 2. [column name (day)] 3. == Key word (Monday)
#
# # Getting a day with a maximum temp
# # print(data[data.temp == data["temp"].max()])
#
# # Getting an element from a particular day
# monday = data[data.day == "Monday"]
# monday_temp_F = monday.temp * 9/5 + 32
# print(monday_temp_F)
#
#
# # Create a dataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Black = 0
# Cinnamon = 0
# Gray = 0
#
# Fur = data["Primary Fur Color"]
# for fur in Fur:
#     if fur == "Black":
#         Black += 1
#     elif fur == "Gray":
#         Gray += 1
#     elif fur == "Cinnamon":
#         Cinnamon += 1

Gray = data[data["Primary Fur Color"] == "Gray"]
Red = data[data["Primary Fur Color"] == "Cinnamon"]
Black = data[data["Primary Fur Color"] == "Black"]

fur_colors = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [Gray, Red, Black],
}

Fur_file = pandas.DataFrame(fur_colors)
Fur_file.to_csv("squirrel_count.csv")
