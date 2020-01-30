import csv

max_list = []
min_list = []
with open("Norman2016.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        minimum = row["TMIN"]
        maximum = row["TMAX"]
        if float(maximum) > -10.0:
            max_list.append(float(row["TMAX"]))
        if float(minimum) > -10.0:
            min_list.append(float(row["TMIN"]))










print("This is the maximum temp in 2016", round(max(max_list)))
print("This is the minimum temp in 2016", round(min(min_list)))
    
print("The avg high temp in 2016", sum(max_list)/len(max_list))
print("The avg high temp in 2016", sum(min_list)/len(min_list))    





    


