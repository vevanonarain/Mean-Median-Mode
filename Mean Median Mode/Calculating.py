import csv
from collections import Counter

with open("weight-height.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

def mean():
    n = len(new_data)
    total = 0

    for x in new_data:
        total = total + x

    mean = total / n
    print("Mean (Average) is -> " + str(mean))

def median():
    n = len(new_data)
    new_data.sort()

    if n % 2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2 - 1]) 

        median = (median1 + median2) / 2

    else:
        median = float(new_data[n//2])

    print("Median is -> " + str(median))

def mode():
    data = Counter(new_data)
    mode_range = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0
    }

    for weight, occurrence in data.items():
        if 75 < float(weight) < 85:
            mode_range["75-85"] += occurrence
        elif 85 < float(weight) < 95:
            mode_range["85-95"] += occurrence
        elif 95 < float(weight) < 105:
            mode_range["95-105"] += occurrence
        elif 105 < float(weight) < 115:
            mode_range["105-115"] += occurrence
        elif 115 < float(weight) < 125:
            mode_range["115-125"] += occurrence
        elif 125 < float(weight) < 135:
            mode_range["125-135"] += occurrence
        elif 135 < float(weight) < 145:
            mode_range["135-145"] += occurrence
        elif 145 < float(weight) < 155:
            mode_range["145-155"] += occurrence
        elif 155 < float(weight) < 165:
            mode_range["155-165"] += occurrence
        elif 165 < float(weight) < 175:
            mode_range["165-175"] += occurrence

    modeRange, modeOccurrence =  0, 0

    for range, occurrence in mode_range.items():
        if occurrence > modeOccurrence:
            modeOccurrence = occurrence
            modeRange = [int(range.split("-")[0]), int(range.split("-")[1])]

    mode = float((modeRange[0] + modeRange[1]) / 2)
    print("Mode is -> " + str(mode))

mean()
median()
mode()