# creation of object of file
path = "Module_1/W2/Assets/"
file = open(path+"Example.txt ",'r')

# reading entire file
# content = file.read()
# print("Entire Content : ", content)

# reading first 100 charachter
# first_100_chars = file.read(100)
# print("First 100 char of file : ", first_100_chars)
# line1 = file.readline()
# line2 = file.readline()

# print(f"Line 1: {line1}")
# print(f"Line 2: {line2}")


# Reading all lins into a list
all_lines=file.readlines()
print(f"Total lines: {len(all_lines)}")
for line in all_lines:
    print(f"line: {line.strip()}")
    

#itarreting through file object 
for line in file :
    print(f"line: {line.strip()}")
    file.close()

