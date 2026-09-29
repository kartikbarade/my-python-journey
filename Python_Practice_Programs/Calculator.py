num1 = float(input("Enter your 1st number : "))
num2 = float(input("Enter your 2nd number : "))

operator = input("Enter operator (+,-,*,/) : ")

match operator:
    case "+":
        print("Addition : ", num1 + num2)

    case "-":
        print("Subtraction : ", num1 - num2)

    case "*":
        print("Multiplication : ",num1 * num2)

    case "/":
        if num2 != 0:
            print("Division : ", num1/num2)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid Choice")
