#dictionaries, it stores word meaning pairs, word is 'key' and meaning is 'value of key'
#we can store diff datatypes in 'value', we can also store list and tuples
#in key we can't add mutable only immutable, like str, bool,int,tuple,,float, NOT list bcz it is mutable
info = {
    "name" : "shagufi",
    "subjects" : ["CS", "Maths"],
    "topics" : ("dict", "sets"),
    "age" : 18,
    "is adult" : True,
    "marks" : 94.5
}

print(info)
print(type(info))

#PROP OF DICT
#there is no order in dict,bcz it has no index unlike tuple,list,str
#dict is mutable
#can't create duplicate 'keys', one key has diff values but can't repeat keys
#if we wanna accese the vale of key, dict["key"]

dict = {
    "name" : "shagufi",
    "subjects" : ["CS", "Maths"],
    "topics" : ("dict", "sets"),
    "age" : 18,
    "is adult" : True,
    "marks" : 94.5
}

print(dict["name"])
print(dict["marks"])

#change the vale of a key
dict["name"] = "shagun"
print(dict)

#we can also add a new key value pair to dict
dict["surname"] = "ali" #it is add in dict in last
print(dict)

null_dict = {} #empty dict is defined then we strt adding key values here
print(null_dict)

#nested dictionaries, we can create dict inside dictionary
student = {
    "name" : "shsgufi",
    "sujects" : {
        "phy" : 60,
        "maths" : 70,
        "chem" : 80
    }
}
print(student) #printing whole dict
print(student["sujects"]) #printing subjects
print(student["sujects"]["chem"])  #printing only chem marks

#DICTIONARY METHODS

#dict.keys(), it returns all keys
student = {
    "name" : "shsgufi",
    "sujects" : {
        "phy" : 60,
        "maths" : 70,
        "chem" : 80
    }
}

print(student.keys()) #not nested keys only outerlayer ones
print(list(student.keys())) #now the keys print in list format
#we can find number of key value pair in both ways
print(len(student))
print(len(list(student.keys())))

#dict.values(), it gives all values
print(student.values())
print(list(student.values())) #converted to list

#dict.items, it returns all key-value pairs as tuple, (key,value)
print(student.items())
print(list(student.items()))

#we can also acess the ky val tuple
pairs = list(student.items()) #here key val tuple converted to  list
print(pairs[0]) #(name,shagufi)
print(pairs[1]) 

#dict.get("key"), return val of key, it is useful bcz if we write a key which doen't exist in dict it returns 'NONE' instead of error
print(student["name"]) 
print(student.get("name"))
print(student.get("time")) #none

#dict.update(newdict), it add the key val pairs(whiich we pass through it) adds to ours dict
student.update({"city" : "dehradun", "age" : "18"})
print(student)
#OR
new_dict = {"surname" : "ali"}
student.update(new_dict)
print(student)
#if we write  same 'key' with diff 'value' so its value updated not created anything new 
student.update({"name" : "shagun"})
print(student)


#SETS,collection of unordered items(no index), each element must be unique and immutable, BUT set is mutable we can add/remove element from it
#in sets we can store a immutable things, like bool,int,float,str,tuple, but NEVER list and dict bcz they are mutable
#hashable val: immutable, unhashable val:mutable
collection = (1, 2, 3, "hello")
print(collection)
print(type(collection)) #set

#if we store multiple value in set, so it simply ignores the duplicate values
collection2 = {1, 2, 2, 3, "hello", "hello"}
print(collection2) #{1, 2, 3, 'hello'}
print(len(collection2)) #len also ignores the duplicate items

empty_set = set() #empty set syntax
print(type(empty_set))

#sets methods
#set.add(elemeent), adds element in set
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hello")
collection.add((1, 2, 3))
print(collection) #it prints 2 only one time

#set.remove(element), removes the element from set
collection.remove(1)
print(collection)
#if we remove something from set which is not there, then it gives error

#set.clear(), it empties the set
collection.clear()
print(collection) # printing empty set

#collection.pop(), it removes a random value
collection = {"shagufi", "ali", "python", "dehradun"}
print(collection.pop()) #removes a random val everytime runs
print(collection.pop())
print(collection)

#set1.union(set2), combines both set values and retuns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2)) #{1, 2, 3, 4}, it returns the new set, can't make any changes in previous ones
print(set1) #printing as it is
print(set2)

#set1.intersection(set2), combines common values and returns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2)) #{2,3}, it returns the new set, can't make any changes in previous ones









