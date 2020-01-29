#import data
#parse data from file
import csv
filename = open("Norman2016.csv")
filedata = csv.reader(filename)
weather_data = []
for i in filedata:
    weather_data.append(i)

#remove useless data
#remove data from inner lists
list_index_correction = 0
tmax = True
for i in range(len(weather_data)):
    for j in range(len(weather_data[i])):
        if weather_data[i][j - list_index_correction] == 'YEAR' or weather_data[i][j - list_index_correction] == 'MONTH' or weather_data[i][j - list_index_correction] == 'DAY' or weather_data[i][j - list_index_correction] == 'STID' or weather_data[i][j - list_index_correction] == 'TMAX' or weather_data[i][j - list_index_correction] == 'TMIN' or weather_data[i][j - list_index_correction] == '2016' or weather_data[i][j - list_index_correction] == 'NRMN':
            del weather_data[i][j - list_index_correction]
            list_index_correction += 1
        elif weather_data[i][j - list_index_correction] == '-996.00' and tmax:
            weather_data[i][j - list_index_correction] = '0'
            tmax = False
        elif weather_data[i][j - list_index_correction] == '-996.00' and tmax != True:
            weather_data[i][j - list_index_correction] = '0'
    list_index_correction = 0
    tmax = True
#remove empty lists
for i in range(len(weather_data)):
    if len(weather_data[i - list_index_correction]) == 0:
        del weather_data[i]
        list_index_correction += 1

#get averagee temperature, min and max temps
num_of_nums = 0
tmax = 0
tmin = 0
highest = float(weather_data[0][2])
lowest = float(weather_data[0][3])
#average tmax
for i in range(len(weather_data)):
    if float(weather_data[i][2]) != 0:
        tmax += float(weather_data[i][2])
        num_of_nums += 1
tmax = float(tmax/num_of_nums)
num_of_nums = 0
#average tmin
for i in range(len(weather_data)):
    if float(weather_data[i][2]) != 0:
        tmin += float(weather_data[i][3])
        num_of_nums += 1
tmin = float(tmin/num_of_nums)
num_of_nums = 0
#highest temp
for i in range(len(weather_data)):
    if float(weather_data[i][2]) > highest and float(weather_data[i][2]) != 0:
        highest = float(weather_data[i][2])
#lowest temp
for i in range(len(weather_data)):
    if float(weather_data[i][3]) < lowest and float(weather_data[i][2]) != 0:
        lowest = float(weather_data[i][3])

#report data
print ("The highest temperature for 2016 in Norman is " + str(highest) + ".")
print ("The lowest temperature for 2016 in Norman is " + str(lowest) + ".")
print ("The highest average temperature for 2016 in Norman is " + str(tmax) + ".")
print ("The lowest average temperature for 2016 in Norman is " + str(tmin) + ".")
