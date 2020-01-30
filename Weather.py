import csv

max_list = []
min_list = []

with open("Norman2016.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")
    for row in reader:
        minimum = row["TMIN"]
        maximum = row["TMAX"]
        if float(maximum) > -20.0:
            max_list.append(float(row["TMAX"]))
        if float(minimum) > -20.0:
            min_list.append(float(row["TMIN"]))

print("The maximum temp in 2016 was", (max(max_list)))

print("The minimum temp in 2016 was", (min(min_list)))

print("The average high temp in 2016 was", sum(max_list)/len(max_list))

print("The average low temp in 2016 was", sum(min_list)/len(min_list))


                            
