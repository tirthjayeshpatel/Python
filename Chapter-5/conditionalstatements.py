#Conditonal Statements
#It allows to execute the code based on the condition evaluates to True or False.

#Types of Conditional Statement
#1.if statement
#2.if else statement
#3.if elif else statement
#4.nested if else statement
#5.Conditional expression (Ternary Operator)

#1. if statement
#syntax:- if condition:
             #code1

#example
age=20
if age>=18:
    print('You can Vote!')


#2. if else statement
#syntax:- if condition:
             #code1
#         else:
             #code2

#example
age=20
if age>=18:
    print('You can Vote!')
else:
    print('You are not eligible for Voting')

#3. if elif else statement
#syntax:- if condition1:
             #code1
#         elif condition2:
             #code2
#         else:
             #code3

#example
number=20
if number>0:
    print(f"{number} is positive")
elif number<0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

#4.nested if else
#syntax:- if condition1:
#           if condition:
               #code1
#           else:
               #code2
#         else:
#             if condition:
                #code3
#             else:
                #code4

num=int(input('Enter a number '))
if num>0:
    if num%2==0:
       print('number is positive and even')
    else:
       print('number is positive and odd')
               
else:
    if num==0:
       print('number is zero')
    else:
       print('number is negative')


#5. Conditional expression(Ternary operator)
 
 #syntax:- value_if_true if condition else value_if_false

age=18
status="adult" if age>=18 else "minor"
print(status)