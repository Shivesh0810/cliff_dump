import math

try:
    print("INSTRUCTIONS")
    print(" 1 = Addition \n 2 = Subtraction \n 3 = Multiplication \n 4 = Division \n 5 = Remainder \n 6 = Power \n 7 = Trignometry \n 8 = Logarithm")
    print("Type exit to exit the program at any time")
    operation = int(input("Enter the operation = "))
    x, k = 0, 1
    while True:
        if(operation == 1):
            y = float(input("Enter the number to add:"))
            x += y
            print(x)
            continue
        if(operation == 2):
            y = float(input("Enter the number to subtract:"))
            x -= y
            print(x)
            continue
        if(operation == 3):
            y = float(input("Enter the number to multiply:"))
            k *= y
            print(k)
            continue
        if(operation == 4):
            y = float(input("Enter the dividend:"))
            z = float(input("Enter the divisor:"))
            a = y / z
            print(a)
            continue
        if(operation == 5):
            y = float(input("Enter the dividend:"))
            z = float(input("Enter the divisor:"))
            a = y % z
            print(a)
            continue
        if(operation == 6):
            y = float(input("Enter the number:"))
            z = float(input("Enter the power:"))
            a = math.pow(y, z)
            print(a)
            continue
        if(operation == 7):
            print("Trignometric list - \n sin , cos , tan , cosec , sec , cot")
            t = input("Enter from the list = ")
            trigo = ["sin", "cos", "tan", "cosec", "sec", "cot"]
            if t in trigo:
                angle = float(input("Enter the angle (in degress) = "))
                angle = angle * math.pi/180
                if t == "sin":
                    print(math.sin(angle))
                if t == "cos":
                    print(math.cos(angle))
                if t == "tan":
                    print(math.tan(angle))
                if t == "cosec":
                    f = 1 / math.sin(angle)
                    print(f)
                if t == "sec":
                    f = 1 / math.cos(angle)
                    print(f)
                if t == "cot":
                    f = 1 / math.tan(angle)
                    print(f)
            else:
                print("Please type from the list")
                exit()
        if(operation == 8):
            num = float(input("Enter the number = "))
            choice = input("Do you want to specify the base? (yes/no)= ")
            if choice == "yes":
                base = float(input("Enter the base = "))
                print(math.log(num, base))
            elif choice == "no":
                print(math.log(num))
            else:
                print("There is something wrong in the input!")
        if(operation > 8) or (operation < 1):
            print("Please enter from the list given above")
            break
except ValueError:
    print("Program ended")
