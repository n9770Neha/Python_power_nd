# CSV file handling
import csv
path = "Module_1/W2/assets/"

# writing into csv file
# with open(path+"employee.csv", 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["id", "name", "department", "salary"])
#     writer.writerow(["1", "Tripan", "HR", 50000])
#     writer.writerow(["2", "Neha", "Engineering", 60000])
#     writer.writerow(["3", "Debo", "Marketing", 45000])
#     writer.writerow(["4", "Priya", "Marketing", 55000])

# reading from csv file
# with open(path+"employee.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"Row: {row}")


# Usung DictReader to read from CSV
# with open(path+"employee.csv", 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(f"{row['name']} works in {row['department']}")

# writing dictionaries to csv
print("------writing dictionaries to csv------")
employees = [
    {'Name':'Suvendu', 'Age':30, 'City':'Ghatal'},
    {'Name':'Ramdas', 'Age':40, 'City':'Mecheda'},
    {'Name':'Anurag', 'Age':25, 'City':'Rajbari'}
]

with open(path+"emp_city.csv", 'w', newline='') as new_file:
    fieldNames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(new_file, fieldnames = fieldNames)
    writer.writeheader()
    writer.writerows(employees)