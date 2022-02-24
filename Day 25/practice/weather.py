import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# data_series = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())

# print(data.temp)

# Prints row with highest temperature
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday)

# monday.temp = monday.temp * 9 / 5 + 32
# print(monday)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Billy"],
    "scores": [76, 81, 39]
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("new_data.csv")