#TYPES OF OPERATORS

#1.ARITHMETIC OPERATORS

a=5
b=3
print(a+b) #(a.)Addition
print(a-b) #(b.)Subtraction
print(a*b) #(c.) Multiplication
print(a/b) #(d.) Division
print(a%b) #(e.) Modulo (remainder)
print(a//b) #(f.) Floor division
print(a**b) #(g.) Exponent 


#2.Comparision OPERATORS

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#3.Assignment OPERATORS
a=3
a+=3
print(a)
a-=3
print(a)
a*=3
print(a)
a/=3
print(a)
a%=3
print(a)
a//=3
print(a)
a**=3
print(a)

#4.Logical OPERATORS
a=3
print(a>2 and a<5)
print(a>2 or a<5)
print(not(a>2 and a<5))

#5. Identity and membership operator
#Identity
a=3
b=2
print(a is b)
print(a is not b)

#Membership
print("a" in "apple")        # True
print("z" not in "banana" )  # True

#6. Bitwise 
a = 5
b = 3

print(a & b)   # 1  (0101 & 0011 = 0001)
print(a | b)   # 7  (0101 | 0011 = 0111)
print(a ^ b)   # 6  (0101 ^ 0011 = 0110)
print(~a)      # -6 (~0101 = -(a+1) = -6)
print(a << 1)  # 10 (0101 << 1 = 1010)
print(a >> 1)  # 2  (0101 >> 1 = 0010)
