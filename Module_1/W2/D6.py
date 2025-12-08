# CSV file handling
import csv
path = "Module_1/W2/assets/"

# writing into csv file
with open(path+"employee.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "department", "salary"])
    writer.writerow(["1", "Tripan", "HR", 50000])
    writer.writerow(["2", "Neha", "Engineering", 60000])
    writer.writerow(["3", "Debo", "Marketing", 45000])
    writer.writerow(["4", "Priya", "Marketing", 55000])

# reading from csv file
with open(path+"employee.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Row: {row}")