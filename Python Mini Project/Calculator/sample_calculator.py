try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("what kind of operation do you want to perform\nPress + for Addition\nPress - for Subtraction\nPress * for Multiplicaton\nPress / for division")

    o = input("Enter the Operation: ")

    match o:
        case "+":
            print(f"The result is: {a+b}")
        case "-":
            print(f"The result is: {a-b}")
        case "*":
            print(f"The result is: {a*b}")
        case "/":
            print(f"The result is: {a/b}")
        case defoult:
            print(f"There was an error ")

except Exception as e:
    print("Enter a valid value of a and b")