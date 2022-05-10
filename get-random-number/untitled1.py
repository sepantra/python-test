from random import random
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


userExclusion = input("Enter the exclusion numbers: (divide numbers by --> , )")
exclusionList =(userExclusion.split(","))

expectedNumbers =int( random() * (num2 - num1) + num1)
mainExpectedNumbers = str(expectedNumbers)
isloop=True
while isloop:
    if mainExpectedNumbers not in exclusionList:
        print(mainExpectedNumbers)
        break