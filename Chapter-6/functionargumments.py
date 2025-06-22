#Arguments are the values that are passed in the function call.

#eg:- 
def greetings(name):
        print("Hello",name)
greetings("Tirth")

#Types of Function Arguments
#a. Required Arguments
#b.Default Arguments
#c.Keyword Arguments
#d. Arbitary Arguments
#e. Arbitary Keyword Arguments

#a. Required Argument
#single 
def greetings(name):
        print("Hello",name)
greetings("Tirth")

#multiple
def greetings(coursename,tutor):
        print("Welcome to ",coursename, "by", tutor)
greetings("Python","Rishabh")

#b.Default Arguments- we can assign default values to arguments in a function definition. If a value is not provided when the function is called , the default value is used.
#if we apply value then our value will be printed

#eg:-
def greetings(name="Tirth"):
        print("Welcome",name)
greetings()
greetings("Madhav")

# c.Keyword Arguments=when calling a function, you can specify arguments by parameters name.These are called keyword arguments and can be given in any order.

#eg-
def add(a,b):
    return a+b
result=add(a=100,b=200)
print(result)
result=add(b=200,a=100)
print(result)      

#d. Arbitary Arguments- If you are unsure how many arguments will be passed , use *args to accept any number of positional arguments.
#The arguments are stored in Tuples

#eg:-
def add(*args):
    return sum(args)
result=add(1,2,3,4)
print(result)


#e. Arbitary Keyword Arguments-If you want to pass a variable number of keyword arguments , use **kwargs.
#The arguments are stored in dictionary.

def print_details(**kwargs):
       for key,value in kwargs.items():
            print(f"{key}:{value}")
print_details(name="Madhav",age=26,city="Delhi")
