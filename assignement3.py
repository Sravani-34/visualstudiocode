'''Write a Python program that asks the user to input two numbers and an arithmetic operator (+, -, *, /). Perform the operation and display the result.
	Example : 
	Enter first number: 10 
Enter second number: 5 
Enter an operator (+, -, *, /): * 
Result: 10 * 5 = 50'''
first_number=int(input("enter first number:"))
second_number=int(input("enter second number:"))
operator=(input("Enter an operation (+, -, *, /):"))
if operator=='+':
    result= first_number+second_number
elif operator=='-':
     result=first_number-second_number 
elif operator=='*':
    result=first_number*second_number
elif operator=='/':
    result=first_number/second_number
else:
    print("Please enter correct number")
print(first_number)
print(second_number)
print(operator)
print(f"Result: {first_number} {operator} {second_number} = {result}")




