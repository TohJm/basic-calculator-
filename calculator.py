def calculate(number1, number2):
    return number1 + number2
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    total = calculate(number1, number2)
    print("The first sum is: ", total)

    number3 = int(input("Enter the third number: "))
    number4 = int(input("Enter the fourth number: "))
    calculate(number3, number4)
    total = calculate(number3, number4)
    print("The second sum is: ", total)

except ValueError:
    print("Please enter a number ONLY")




