#Strings are the collection of characters enclosed with in ''," ",''' '''
print('Hello World')
print("Hello World")

#To print along with single quote and double quote

#method-1
print("\"Hello\" \'World\'")
#method-2
print("\"Hello\" 'World'")
#method-3
print('''"Hello, World" ''')

#Formatted String-It is a way to insert variables or expression inside a string.
#There are multiple ways to format strings in python.
#a. old-style formatting(%)
name="madhav"
age=15
print("My name is %s and I am %d" %(name,age))

#b.str.format()
name="Madhav"
age=15
print("My name is {} and I am {}.".format(name,age))

#you can also reference the variables by index or keyword.
print("My name is {0} and I am {1}".format(name,age)) 
print("My name is {name} and I am {age}".format(name="Madhav",age=25))


#c.f string=These are the most efficient way to format string.- we can use both small f and capital F
name="Madhav"
age=13
print(f"my name is {name} and Im {age}")

#you can also perform expression inside the placeholder.
print(f"my age after 5 years will be {age+5}")