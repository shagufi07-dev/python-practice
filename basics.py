# # day-004
# print("Hello World")
# print(5)
# print("byeeee")
# print(8+9)
# print(2*3)
# print("Shagufi Ali")
# print("Shagufi" , "Ali")

# # day-005
# # for a new line \n it is a escape sequence characters 
# print("My name is Shagufi\nMy age is 18") # printing My name is Shagufi
#                                           # My age is 18
# # cmntout shrtcut  select and ctrl+/
# # for multiline cmnt we can also enclosed the lines in tripple single or double quotes or just selcet then ctrl+/

# # \" gives us " if we wanna show it in output (if we want ' so we have to put string also on ')
# print("My name is \"SHAGUFI\"") # printing My name is "SHAGUFI"
# print('My name is \'SHAGUFI\'') # printing My name is 'SHAGUFI'

# print("Hye", 6, 7) # printing Hye 6 7 
# # we can also separate characters bye using sep=
# print("Hye", 6, 7, sep= "~") # printing Hye~6~7
# print("Shagufi", "age", 18, sep="_") # printing Shagufi_age_18

# # if we want something at the end use end=
# print("name", "shagufi", sep="-", end="Bye\n") # if we dont addd \n so the next st. directly print in front of the end st. instead of new line 
# print("age-18")  

# # day-006
# a = 2 # integer int
# b = 1.5 # floating float
# # when we + so the data type is of same type 
# print(a+b)
# c = "shagufi" # string str
# d = True # Boolen bool, also False
# e = None # Nonetype
# f = complex(8, 2) #complex
# print(type(a)) # by using type() we know the datatype
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# # a 'list' is a list of diff datatypes, we can change it means it is mutable
# # a 'tuple' is also same but we can't change it means it is immutable
# # dictionary is key value pairs storage
# list = [8, 3.3, ["apple", "banana"]]
# tuple = (("parrot", "sparrow"), ("rabbit", "lion"))
# dict = {"name":"shagufi", "age":18, "CanVote":True}
# print(list)
# print(tuple)
# print(dict)

# airthmetic operators
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b) # we always get a floating value
print(a % b) # remainder when a/b
print(a ** b) # a^b

# Relational operators, they return a boolen value
a= 50 
b = 20

print(a == b) # False
print(a != b) # True
print(a >= b) # True
print(a > b) # True
print(a <= b) # False
print(a < b) # False

# Assignment operators
num1 = 10
num1 += 5
print("num:", num1) # 15
num2 = 10
num2 -= 5
print("num:", num2) # 5
num3 = 10
num3 *= 5
print("num:", num3) # 50
num4 = 10 
num4 /= 5
print("num:", num4) # 2.0
num5 = 10 
num5 %= 5 # give a remainder when 10/5
print("num:", num5) # 0
num6 = 10
num6 **= 5 
print("num:", num6) # 10^5

# Logical operator
print(not False) #True
print(not True) #False

a = 20
b = 10 
print(not (a>b)) #False
print(not (a<b)) #True

val1 = True
val2 = True
val3 = False
val4 = False
#and opt. only gives true when both are True
print("and operator:", val1 and val2 ) #True
print("and operator:", val1 and val3)  #False
print((a==b) and (a>b)) #False

#or opt. gives True when both or eithr one are True
print("or operator:", val1 or val3) #True
print("or operator:", val3 or val4) #False
print((a==b) or (a>b)) #True

#Type conversion, automatic conversion to superior value
a = 2
b = 4.25 
print(a + b) #2.0 + 4.25 = 6.25

#Type casting, manual conversion
#int(val) == int
#float(val) == float
#str(val) == str
a = "2" #str
b = 4.25 #int
a = int(a) #now a = 2, which is int
print(a + b)

#taking input from user
# name = input("name:")
# age = input("age:")
# DOB = input("DOB:")
# print("VEERIFIED")
# print("Welcome", name, sep = "~") #printing Welcome~name

# val1 = input("enter val1:")
# print(type(val1), val1) #when we take a val as input it convert in str

# val2 = int(input("enter val2:")) #now it just convet it in int
# print(type(val2), val2)

# val3 = float(input("enter val3:")) #it convert to float
# print(type(val3), val3)











