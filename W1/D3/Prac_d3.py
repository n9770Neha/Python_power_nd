#Function
# def greet(name):
#     return "hello, "+ name+"!"
# user_name=input("Enter your name: ")
# print(greet(user_name))


#Factorial Calculation using Recurrtion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a positive num:"))
if num<0 :
    print(" Factorial of negetive num not possible")
else:
    print(f"The factorial of {num} is {factorial(num)}")


#generate fibonnaci useing function
#prime number 
