# 1. Integer
a=123
print(a)
print(type(a))

#2. Float
a=1.456
print(a)
print(type(a))

#3.Complex
a=complex(3,5)
print(a)
print(type(a))

#4.String
a="hello"
b='world'
print(a)
print(b)
print(type(a))
print(type(b))

#Note:- String+String=String
c=a+b
print(c)

#for giving space
c=a+" "+b
print(c)

#5.List-mutable, multiple datatype
l=[1,2,"tirth",True]
print(l)
print(type(l))

#6.Tuple-immutable, multiple datatype
t=(1,2,"tirth",True)
print(t)
print(type(t))

#7.Dictionary-key value pair
a={"name":"tirth" , "age":20 }
print(a)
print(type(a))

#8. Set-unordered collection of elements , no duplicates,mutable
a={1,2,3}
print(a)
print(type(a))
b={1,2,"tirth",True}
print(b)
print(type(b))

#9.Boolean-True, False
a=True
b=False
print(a)
print(b)
print(type(a))
print(type(b))
print(a+b)