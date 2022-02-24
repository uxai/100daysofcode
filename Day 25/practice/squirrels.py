import pandas

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(df[df["Primary Fur Color"] == "Gray"])
red_squirrels = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

new_df = pandas.DataFrame(data_dict)
new_df.to_csv("squirrel_fur.csv")