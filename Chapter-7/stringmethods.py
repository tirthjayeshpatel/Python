#String Methods

s="Hello world"

#1. len()
print(len(s))

#2.upper()
print(s.upper())

#3.lower()
print(s.lower())

#4.title()
print(s.title())

#5.capitalize()
print(s.capitalize())

#6.count()
print(s.count("Hello"))

#7.find()
print(s.find("Hello"))

#8.replace()
print(s.replace("world","there"))

#9.split()
print(s.split())

#10.join()
words=["hello","world"]
print("".join(words))

#11.strip()
h=" hello "
print(h.strip())

#12.startswith()
print(s.startswith("Hello"))

#13.endswith()
print(s.endswith("world"))

#14.isalpha()
a="tirth"
b="tirth patel"
print(a.isalpha())
print(b.isalpha()) #because space is not considered as alphabet

#15.isdigit()
c="123"
print(c.isdigit())
d="123 "
print(d.isdigit()) #because space is not considered as alphabet

#16.isupper()
print(s.isupper())

#17.islower()
print(s.islower())