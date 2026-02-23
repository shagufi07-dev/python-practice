#List in python
#in list we can store diff datatypes value

marks = [95.5, 82.3, 70.5, 56.3, 45.7] #list
print(marks)
print(type(marks)) #type is list
print(len(marks)) #5

#list properties are similar to str, like access to particular character by indexing
print(marks[0]) #95.5
print(marks[1]) #82.3

student = ["Krana", 95.5, 17, "Noida" ]
print(student)

#the diff in str and list is that str is immutable and list is mutable, means we can make chagne in the list
str = "hello" #here we only accese the chr by inddexing not make changes
student = ["Krana", 95.5, 17, "Noida" ] 
student[0] = "Arjun" #here we can make cahnges
print(student)

#in list only accese the index till they are, means no extras
# print(student[5]) it gives error

#List Slicing, similar to str sclicing
#list_name[starting_index:ending_index], ending idx is not included
marks = [85, 94, 76, 63, 48]
print(marks[1:4]) #[94,76,63]
print(marks[:4]) #[85,94,76,63]
print(marks[1:]) #[94,76,63,48]
#also have negative index in slicing list like str
print(marks[-3:-1])  #[76,63]

#List methods/functions

#list.append.(), it adds the value(which we pass through it) in list's ends
list = [2, 1, 3]
list.append(4) #adds '4' at lasts
print(list)

#list.sort(), it arrange the list in ascending order
list = [2, 1, 3]
list.append(0)
list.sort()
print(list)
#print(list.sort()/list.append()),, we don't use them like this, it only rturs us "NONE"
#str chr list also sortable, they sort by the first letter 
list = ["a", "z", "d", "f"]
list.sort()
print(list)

list = ["shagufi", "apple", "mango"]
list.sort()
print(list)

#list.sort(reverse=True), list sorts in descending order
list = [2, 1, 3]
list.sort(reverse=True) #list sorts in descending order, applicable on str list also
print(list)

#list.reverse(), it reverse the list
list = ['a', 'z', 'd']
list.reverse()
print(list)

#list.insert(indx,chr), it insert chr in list on particular index, the old chr on that index shifts not removed
list = [2, 1, 3]
list.insert(2,8) #[2,1,8,3]
print(list)

#list.remove(), remove the first occurance of an element which we pass through it
list = [2, 1, 3, 1]
list.remove(1) #it removes first '1'
print(list) #[2,3,1]

#listpop(indx), remove element at particular index
list = [2, 1, 3, 1]
list.pop(2) #removes 3 as it on indx 2
print(list) #[2,1,1]

#TUPLES in python
#tuple is immutable like str, we can't make cahnges

tup = (2, 1, 3, 1)
print(type(tup)) #type is tuple
print(tup[0]) #2
print(tup[2]) #3
print(tup[-1]) #1

#empty tuple is also valid
tup = ()
print(tup)
print(type(tup)) 

#if we wanna make single val tuple so it should has a comma(,) in last otherwise python thinks its a int/float/str
tup = (1,)
tup2 = ("shagufi",)
print(type(tup))
print(type(tup2))

#slicing works same 
tup = (2, 1, 3, 1)
print(tup[0 : 3]) #(2,1,3)

#tuple method/function
#tuple.index(element), returns index of first occurnace of element which we pass through it
tup = (2, 1, 3, 1)
print(tup.index(2)) #0

#tuple.count(element), counts total occurance of that element
tup = (2, 1, 3, 1)
print(tup.count(1)) #2