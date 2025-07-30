
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

#ask user for operation
operation=input("Enter operation(+,-,*,/):")

#performa calcu based on the operation that has been selcted
if operation=="+":
    result=num1+num2
    print(f"{num1}+{num2}={result}")
    
elif operation=="-":
    result=num1-num2
    print(f"{num1}-{num2}={result}")
elif operation =="*":
    result=num1*num2
    print(f"{num1}*{num2}={result}")
elif operation=="/":
    if num2!=0:
        result=num1/num2
        print(f"{num1}/{num2}={result}")
    else:
        print(" Erro:Math errr occured")