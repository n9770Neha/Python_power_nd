# error handling in file operation
# 1. FileNotFoundError
# 2. PermissionError
# 3. IsADirectoryError
# 4. IOError

# basic try-except block
try:
    file = open("nonexistance.txt", 'r')
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("No permission to read ")
except Exception as e:
    print(f" An unexpected error occured: {e}") 

# complete try except else finally
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileExistsError:
    print("File not found, creating a new file...")
    file = open('data.txt', 'w')
    file.write("Default content ")
    content = "kjdhgjdfhjdhfk ajgfahjfgdhf jhfgjhgsd"
except IOError as e:
    print(f"Input / Output error: {e}")
else:
    print("File read successfully")
    print(f"File content length : {len(content)}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup completed....") 

# using with statement with error handling
try:
    with open('data.txt', 'r') as file:
        content = file.read()
        result = 10/0
except FileNotFoundError:
    print("File not found.")
except ZeroDivisionError:
    print("Math error occured.")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Operation successful.")