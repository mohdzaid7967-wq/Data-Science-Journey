while True:
    try:
        a = int(input("Enter the number 1: "))
        b = int(input("Enter the number 2: "))
        print(f"The devision of two number is {a/b}")
    
    except ValueError:
        print("Do not use other type for calculation!")
    
    except ZeroDivisionError:
        print("Do not divide by zero!")
    
    except Exception as e:
        print("Some Error Occured!",e)