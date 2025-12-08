#SIMPLE CALCULATER PROB
# num1 = float(input("Enter 1st num: "))
# operator = input("Enter operator(+,-,*,/): ")
# num2 = float(input("Enter second num: "))
# if operator=="+":
#     result=num1 + num2
# elif operator=="-":
#     result=num1 - num2
# elif operator=="*":
#     result=num1 * num2
# elif operator=="/":
#     if num2 !=0:
#      result =num1 / num2
#     else:
#        result= " Error!"
# else:
#    result="Invalid operator"
# print(f"Result:{result}")
    


#iterative calculator program
while True:
    num1 = input("Enter first number (or 'exit' to quit): ")
    if num1.lower() == 'exit':
        break

    operator = input("Enter operator (+, -, *, /): ")
    num2 = input("Enter second number: ")

    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")