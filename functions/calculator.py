try:
    def addition(num1, num2):
        return num1 + num2

    def substraction(num1, num2):
        return num1 - num2

    def multiplication(num1, num2):
        return num1*num2

    def division(num1, num2):
        return num1 / num2

    print('''\nSelect an Operation to be performed\n
1.Addition\n
2.Substraction\n
3.Multiplication\n
4.Division
''')
    choice = input("Enter Choice[1/2/3/4]: ")
    num1 = int(input("Enter Your number 1: "))
    num2 = int(input("Enter Your number 2: "))


    if choice == '1':
        print(addition(num1, num2))
    elif choice == '2':
        print(substraction(num1, num2))
    elif choice == '3':
        print(multiplication(num1, num2))
    elif choice == '4':
        print(division(num1, num2))
    else:
        print("Invalid Input!")

except ZeroDivisionError:
    print("Not divisible by Zero!")
except ValueError:
    print("Please Input Numbers!")

else:
    print("Calculation Completed")