# Q1: what is expected output and reason?

value = None

if value:
   print("Value is True")
else:
   print("Value is False")

#reason:- because None means nothing is stored in value variable. Instead of None if there is false,0,0.0,'',[],{},set() then also it will return value is false

#Q2: write a simple program to determine if a given year is a leap year using user input.

year=int(input("enter year "))
if (year%4==0 and year%100!=0) or (year%400==0):
   print(f"{year} is leap year")
else:
   print(f"{year} is not a leap year")


#Q-3.login autnentication using conditional statement. Assume you have a predefined username and predefined password.
#write a program that prompts the user to enter a username and password and checks whether they match. Provide appropriate message for following cases:
# both username and password are correct
# username is correct but password is incorrect
# username is incorrect
 

predefined_username="Madhav"
predefined_password="Pass@123"

username=input("enter username ")
password=input("enter password ")

if username==predefined_username:
   if password==predefined_password:
      print("Login successfully")
   else:
      print("Incorrect Password")
else:
   print("invalid username")


#Q-4. Admission eligibility-  Auniversity has following eligibility criteria for admission:
# marks in maths>=65
# marks in physics>=55
# marks in chemistry>=60
# total marks in all three subjects >=180 OR total marks in maths and physics >=140.
# WAP that takes marks in three subjects as input and prints whether the student is eligible for admission.

print("enter marks from 100") 
physics=int(input("enter physics marks"))
chemistry=int(input("enter chemistry marks"))
maths=int(input("enter maths marks"))

if (maths>=65 and physics>=55 and chemistry>=50 and (physics+chemistry+maths>=180))or (maths+physics>=140):
   print("you are eligible!")
else:
   print("you are not eligible!")
