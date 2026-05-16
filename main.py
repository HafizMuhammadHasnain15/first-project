name=input("enter your name : ")
print(name.capitalize())

num1=float(input("enter the first number : "))
num2=float(input("enter the  second number : "))

symbol=input("enter the symbol : ")
if symbol =="+":
    print(num1 + num2)
elif symbol == "-":
    print(num1 - num2)
elif symbol == "*":
    print(num1 * num2)
elif symbol =="/":
    if num2==0:
        print("not possible ")
    else:
        print(num1/num2)
else:
    print("wronge input")