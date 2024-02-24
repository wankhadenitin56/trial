def add (a,b):
    c=a+b
    return (c)
    
def sub(a,b):
    c=a-b
    return(c)
def mult(a,b):
    c=a*b
    return(c)

def devide(x,y):
    if y==0:
        print("can not devided with 0")

    else:
        c=x/y
        return()
    
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice =='5':
        print(" u r existing the programme, byyyyyy" )
        break
    

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mult(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", devide(num1, num2))
        break
    else:
        print("Invalid Input")
