def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b==0:
        return "Error! Divide by Zero."
    return a / b
def modulus(a,b):
    return a % b
def power(a,b):
    return a ** b
def calculate():
    print("=====simple python calculator=====")
    print("select an operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.modulus")
    print("6.power")
    print("7.Exit")

    while True:
        choice=input("\nEnter choice (1-7):")

        if choice =="7":
            print("Exiting calculator.. Goodbye!")
            break
        if choice in ['1','2','3','4','5','6']:
            try:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))

            except ValueError:
                print("invalid input! please enter numbers only.")
                continue
            if choice =='1':
                print(f"the result is:{add(num1,num2)}")
            elif choice =='2':
                print(f"the result is:{subtract(num1,num2)}")
            elif choice =='3':
                print(f"the result is:{multiply(num1,num2)}")
            elif choice =='4':
                print(f"the result is:{divide(num1,num2)}")
            elif choice =='5':
                print(f"the result is:{modulus(num1,num2)}")
            elif choice =='6':
                print(f"the result is:{power(num1,num2)}")

        else:
            print("invalid choise! please select valid option.")


calculate()
                
            

