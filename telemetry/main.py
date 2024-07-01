# Import json and system module
import json
import sys

# Data set is pretty large, so I set the recursion limit to a large number 
sys.setrecursionlimit(1000000)

# Load json file
myFile = open("telemetry.json")
data = json.load(myFile)

# Create empty dictionary
telemetryData = {}

# Load JSON data into Python dictionary
dataList = data["telemetry"]
for i in range(0, len(dataList)):
    telemetryData[i] = dataList[i]

# Convert Python dictionary to a list
telemetryDataAsList = []
for i in range(0, len(telemetryData)):
    telemetryDataAsList.append(telemetryData[i])

# Using recursion to find maximum velocity 
def findMax(listSoFar, parameter):
    # Base Case: If the current list only has 0 elements, return 0
    if len(listSoFar) == 0:
        return 0
    # Another Base Case: If the current list has 1 element, return it's max
    elif len(listSoFar) == 1:
        return listSoFar[0][parameter]
    # Recursive Case
    else:
        max = findMax(listSoFar[1:], parameter)
        if max > listSoFar[0][parameter]:
            return max
        else:
            return listSoFar[0][parameter]

# Finding maximum velocity and altitude
def main(data):
    print("Maximum Altitude: ", findMax(data, "altitude"))
    print("Maximum Velocity: ", findMax(data, "velocity"))

main(telemetryDataAsList)

# Closing the file 
myFile.close()