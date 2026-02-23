#Set and Dictionary question practice

#Question 1: store val in dict
dictionary = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(dictionary)


# ==========================================================================================


#Question 2: given a list of subs for students. Assume one classroom is required for 1 sub.
# how many classrooms are needed by all students
subjects = {"python", "java", "C++", "python", "javascript", 
            "java", "python", "java", "C++", "C"
            }
print("No. of classrooms required: ", len(subjects)) #we required ujique classrooms as much as unique subjects


#=================================================================================================


#Question 4: figure out way to store  9 & 9.0
values = {9 , 9.0}
print(values) #here it gives only 9, bcz it treats both as same
#1, store one as str
values = {"9", 9.0}
print(values)
#2, we can store as tuple with thier datatypes
values = {
    ("float", 9.0), 
    ("int", 9)
}
print(values)


#===========================================================================================


#Question 5: Unique username checker
a = input("First username: ")
b = input("Second username: ")
c = input("Third username: ")
d = input("Fourth username: ")
e = input("Fifth username: ")

usernames = {
    a, b, c, d, e
}

total_username = [a, b, c, d, e]
print(len(total_username)) # # it give no. total usernames entered 

print(len(usernames)) # # it gives unique username entered

if(len(total_username) != len(usernames)):
    print("Duplicate usernames found")
else:
    print("All usernames are unique")


#================================================================


#Question 6:  Remove Banned Users
banned_users = set()
banned_users.add(input("Banned username 1: "))
banned_users.add(input("Banned username 2: "))
banned_users.add(input("Banned username 3: "))

users = set()
users.add(input("username 1: "))
users.add(input("username 2: "))
users.add(input("username 3: "))
users.add(input("username 4: "))
users.add(input("username 5: "))

allowed = users - banned_users #here we use A-B in sets

print("allowed users: " , allowed)
print("no. of allowed users: ", len(allowed))


#===========================================================================


#Question 7:  common passed studentds
maths_passed = set()

m1 = float(input("student 1 maths cmarks: "))
if(m1 >= 40):
    maths_passed.add("student1")  
m2 = float(input("student 2 maths marks: "))
if(m2 >= 40):
    maths_passed.add("student2")
m3 = float(input("student 3 maths marks: "))
if(m3 >= 40):
    maths_passed.add("student3")
m4 = float(input("student 4 maths marks: "))
if(m4 >= 40):
    maths_passed.add("student4")
m5 = float(input("student 5 maths marks: "))
if(m5 >= 40):
    maths_passed.add("student5")

science_passed = set()

s1 = float(input("student 1 science marks: "))
if(s1 >= 40):
    science_passed.add("student1")
s2 = float(input("student 2 science marks: "))
if(s2 >= 40):
    science_passed.add("student2")
s3 = float(input("student 3 science marks: "))
if(s3 >= 40):
    science_passed.add("student3")
s4 = float(input("student 4 science marks: "))
if(s4 >= 40):
    science_passed.add("student4")
s5 = float(input("student 5 science marks: "))
if(s5 >= 40):
    science_passed.add("student5")


passed_students = maths_passed.intersection(science_passed)
print("passed students", passed_students)


#===========================================================================


#Question 8: unique participants
A1 = input("participant 1 of EVENT A: ")
A2 = input("participant 2 of EVENT A: ")
A3 = input("participant 3 of EVENT A: ")
A4 = input("participant 4 of EVENT A: ")

Event_A = {A1, A2, A3, A4}

B1 = input("participant 1 of EVENT B: ")
B2 = input("participant 2 of EVENT B: ")
B3 = input("participant 3 of EVENT B: ")
B4 = input("participant 4 of EVENT B: ")

Event_B = {B1, B2, B3, B4}

unique_participants = Event_A.union(Event_B)
print("Unique participants: ", unique_participants)


#======================================================================


#Question 9: Weak Paasword Detector
pass1 = input("Password1: ")
pass2 = input("Password2: ")
pass3 = input("Password3: ")
pass4 = input("Password4: ")
pass5 = input("Password5: ")
pass6 = input("Password6: ")

passwords = {pass1, pass2, pass3, pass4, pass5, pass6}
print(passwords)

if(len(passwords) < 6):
    print("Weak: duplicate passwords")
else:
    print("All passwords are unique")


#==================================================================


#Question 10: Remove Random User 
a = input("username 1: ")
b = input("username 2: ")
c = input("username 3: ")
d = input("username 4: ")
e = input("username 5: ")

usernames = {a, b, c, d, e}
print(usernames.pop())
print(usernames)


#===================================================================


#Question 11: Score Analyzer
a = int(input("Score 1: "))
b = int(input("Score 2: "))
c = int(input("Score 3: "))
d = int(input("Score 4: "))
e = int(input("Score 5: "))
scores = {a, b, c, d, e}

print("Highest score: ", max(scores))
print("Lowest score: ", min(scores))
print("Total unique scores: ", len(scores)) 

#================================================================


#Question 12: Student Records (dict + set)
A1 = int(input("Enter roll number of Class A student 1: "))
A2 = int(input("Enter roll number of Class A student 2: "))
A3 = int(input("Enter roll number of Class A student 3: "))
A4 = int(input("Enter roll number of Class A student 4: "))


B1 = int(input("Enter roll number of Class B student 1: "))
B2 = int(input("Enter roll number of Class B student 2: "))
B3 = int(input("Enter roll number of Class B student 3: "))
B4 = int(input("Enter roll number of Class B student 4: "))

records = {
    "classA" : {A1, A2, A3, A4},
    "classB" : {B1, B2, B3, B4}
}
common = records["classA"].intersection(records["classB"])

print("Common students: ", common)


#====================================================================


#Question 13: Login System
r1 = input("Registered username 1: ")
r2 = input("Registered username 2: ")
r3 = input("Registered username 3: ")
r4 = input("Registered username 4: ")
r5 = input("Registered username 5: ")

registered = { r1, r2, r3, r4, r5}

att1 = input("Attempt 1: ")
att2 = input("Attempt 2: ")
att3 = input("Attempt 3: ")

attempt = {att1, att2, att3}

logged_correctly = registered.intersection(attempt)
invalid_login = attempt - registered

print("Logged correctly: ", logged_correctly)
print("Invalid login: ", invalid_login)


#==============================================================


#Question 14: Favorite Numbers
#User enters 7 numbers.
#Store in set.
#Slice the first 3 unique numbers
#and last remaining ones after converting set → list.
#Compare their sums.

num1 = int(input("Enter fav num 1: "))
num2 = int(input("Enter fav num 2: "))
num3 = int(input("Enter fav num 3: "))
num4 = int(input("Enter fav num 4: "))
num5 = int(input("Enter fav num 5: "))
num6 = int(input("Enter fav num 6: "))
num7 = int(input("Enter fav num 7: "))

Fav_nums = {num1, num2, num3, num4, num5, num6, num7}

list_Favnums = list(Fav_nums)
slic1 = list_Favnums[ : 3]
slic2 = list_Favnums[3 : ]  

sum1 = sum(slic1)
sum2 = sum(slic2)

if(sum1 == sum2):
    print("Both slices sum sre Equal")
elif(sum1 > sum2):
    print("Sum of slice 1 is GREATER")
else:
    print("Sum of slice 2 is GREATER")