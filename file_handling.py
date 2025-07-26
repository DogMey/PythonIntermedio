# .txt

import os

txt = open("PythonIntermedio/MyFile.txt", "w+") # "w" mode to write to the file
txt.write("Hola soy kevin")
txt.seek(0)  # Move the cursor to the beginning of the file
print(txt.read())  # Print the content of the file
txt.seek(0)
print(txt.readlines())
txt.seek(0)

for line in txt.readlines():
    print(line)  # Print each line without extra spaces

txt.write("\nQuiero aprender Django")  # Append a new line to the file
txt.readlines()  # Read the lines again

txt.close()  # Close the file to save changes

with open("PythonIntermedio/MyFile.txt", "r") as txt:  # Use 'with' to handle file context
    print(txt.read())  # Read the content of the file

#os.remove("PythonIntermedio/MyFile.txt")  # Remove the file

# .json

import json

data = {
    "name": "Kevin",
    "age": 25,
    "city": "Bogotá",
    "skills": ["Python", "Django", "JavaScript"],
};

with open("PythonIntermedio/data.json", "w+") as json_file:
    json.dump(data, json_file, indent=4)  # Write JSON data to the file
    json_file.seek(0)  # Move the cursor to the beginning of the file
    print(json_file.read())  # Read the lines from the file

with open("PythonIntermedio/data.json", "r") as json_file:
    data = json.load(json_file)  # Load JSON data from the file
    print(data)  # Print the loaded data
    print(type(data))  # Print the type of the loaded data

# .csv

import csv

with open("PythonIntermedio/FileCSV.csv", "w+", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Age", "City"])  # Write header
    writer.writerow(["Kevin", 25, "Bogotá"])  # Write data row
    csv_file.seek(0)  # Move the cursor to the beginning of the file
    print(csv_file.read())  # Read the content of the file
