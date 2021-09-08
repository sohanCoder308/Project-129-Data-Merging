import csv

dataset1 = []
dataset2 = []

with open("bright_stars.csv", "r", encoding="utf-8") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("bright_stars_sorted.csv", "r", encoding="utf-8") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers1 = dataset1[0]
stars_data_1 = dataset1[1:]

headers2 = dataset2[0]
stars_data_2 = dataset2[1:]

headers = headers1 + headers2
stars_data = []

for index, data_row in enumerate(stars_data_1):
    stars_data.append(stars_data_1[index] + stars_data_2[index])

with open("final.csv", "a+", encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)