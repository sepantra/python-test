# taking and storing first number in num1 variable
num1 = int(input("Enter first number: "))
# taking and storing second number in num2 variable
num2 = int(input("Enter second number: "))
# adding the two numbers and storing it in sum variable
operator = (input("Enter the operation { + , - , * , / }: "))

plus = num1 + num2
minus = num1 - num2
multiplication = num1 * num2
divide = num1 / num2

if operator == "+" :
    print(plus)
if operator == "-" :
    print(minus)
if operator == "*" :
    print(multiplication)
if operator == "/" :
    print(divide)