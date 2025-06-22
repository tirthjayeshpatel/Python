#write a python program to create a calculator that can perform at least five different mathematical operations such as addition, subtraction, multiplication, division,and average. Ensure that program is userfriendly , prompting for input and displaying the results clearly.
#(+,-,*,/,average)

#method-1=without using function



num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
operation=input("enter operation(sum,sub,mul,div,average)")

if operation=='+':
    num3=num1+num2
    print(num3)
elif operation=='-':
    num3=num1-num2
    print(num3)
elif operation=='*':
    num3=num1*num2
    print(num3)
elif operation=='/':
    num3=num1/num2
    print(num3)
elif operation=='average':
    avg=(num1+num2)/2
else:
    print("invalid operation")
  
#method-2=with using function

def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=a/b
    return c

def avg(a,b):
    c=(a+b)/2
    return c

print("Operations available 1. SUM , 2.SUB , 3.MUL , 4.DIV , 5.AVG")
a=int(input("enter num1"))
b=int(input("enter num2"))
choice=int(input("select choice"))


if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
elif choice==5:
    print(avg(a,b))
else:
    print("invalid choice")


#another method for method2 storing function call in a variable 

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def avg(a, b):
    return (a + b) / 2

print("Operations available:\n1. SUM\n2. SUB\n3. MUL\n4. DIV\n5. AVG")

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
choice = int(input("Select choice: "))

if choice == 1:
    result = add(a, b)
elif choice == 2:
    result = sub(a, b)
elif choice == 3:
    result = mul(a, b)
elif choice == 4:
    result = div(a, b)
elif choice == 5:
    result = avg(a, b)
else:
    result = "Invalid choice"

print("Result:", result)
