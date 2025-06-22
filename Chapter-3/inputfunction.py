a=input("Enter Name ")
print("hello"+a)

#Homework

#Q-1. Prompting the user for their name and 3 subject marks
Name=input("Enter your name")
maths=int(input("Enter Maths Marks"))
physics=int(input("Enter Physics Marks"))
chemistry=int(input("Enter Chemistry Marks"))

#Q-2. Calculating percentage for 3 subjects
percentage=((maths+physics+chemistry)/300)*100
print(percentage)

#Q-3. Printing the final results
print(f" Hello {Name},Your Maths marks are {maths}, Your Physics marks are {physics},Your Chemistry marks are {chemistry}. Your percentage is {percentage}")


#Q-4. Write a program that collects name ,age, heigth,student status from user input , stores them into dictionary and prints them.

name=input("Name")
age=int(input("age"))
height=input("height")
studentstatus=input("Are u a student(yes/no)?")

userdata={"Name":name,"Age":age,"Height":height,"Studentstatus":studentstatus}
print(userdata)
