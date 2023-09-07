import csv
import json

# csv format
# BUS,License Plate,Driver Name,Driver Number,Helper Name,Helper Number

with open("bus_details.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        if row[0] == "ï»¿BUS" or row[0] == "BUS":
            continue
        print(row)
        data: dict = {
            "bus": {
                "letter": str(row[0]).upper(),
                "license": str(row[1]).upper(),
            },
            "driver": {
                "name": str(row[2]).upper(),
                "phone": str(row[3]).upper(),
            },
            "helper": {
                "name": str(row[4]).upper(),
                "phone": str(row[5]).upper(),
            },
        }
        with open(f"./details/{row[0]}.json", "w") as jsonfile:
            json.dump(data, jsonfile)
