#functions- It is a block of code that performs a specific task.
#we can use function by calling its name
#benefits=increases readability and reusability
#def is used to create function.
#parameters= variables listed inside paranthesis in function definition
#argument= values passed in function call

#Types of Function
#1.built in-predefined functions in python. eg- sum(), print(), input(),max()
#2. userdefined function-we can create our own functions based on our requirement.

#Syntax:- def my_function(parameters)
#              instruction-1
#              instruction-2
#              instruction-3
#         return result


#1. function without parameters
def greetings():
    print("Welcome")
greetings()

#2. function with parameters
def add(a,b):
    c=a+b
    print(c)
add(2,3) #or
add(a=2,b=3)#or
add(b=3,a=2)


#return statement- It is used to place the result back to the place where the function was called.

#eg-1
def add(a,b):
    return a+b
result=add(2,3)
print(result)

#eg-2 celsius to fahrenheit(F=(c*9/5)+32)

def c_to_f(c):
    fahrenheit=(c*9/5)+32
    print(type(fahrenheit))
    return fahrenheit
    
temp=c_to_f(25)
print(temp)


#pass statement- It does nothing and is used when you need to write code that will be added later or to define an empty function

#eg-
def my_function():
    pass