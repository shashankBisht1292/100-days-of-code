import pandas as pd

data_file = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# print(data_file)

total_grey_squirrel = len(data_file[data_file["Primary Fur Color"] == 'Gray'])
total_cinnamon_squirrel = len(data_file[data_file["Primary Fur Color"] == 'Cinnamon'])
total_black_squirrel = len(data_file[data_file["Primary Fur Color"] == 'Black'])

data_dict = {
    "fur_color": ["Grey", "Cinnamon", "Black"],
    "count": [total_grey_squirrel, total_cinnamon_squirrel, total_black_squirrel]
}

df = pd.DataFrame(data_dict)
df.to_csv('./squirrel_color_count.csv', index=False)
print(total_grey_squirrel)