#chapter2

# str1 = "this is a str"
# str2 = 'this is a str'
# str3 = '''this a str'''

print("shagufi\tali") # here it prints with a tab gap
print("shagufi\nali") # here it prints on next line

#concatenation, means adding of two str
name = "SHAGUFI"
Surname = "ALI"
print(name + Surname) #printing SHAGUFIALI 
print(name + " " + Surname) # here we add a blank str means it add gap betwn them 
final = name + " " + Surname
#lenght of str, it counts all the things in a str including space
print(len(name))
print(len(Surname))
print(len(final)) #here it count the gap also

#Indexing, means when a str create all the characters get positions, in python positions starts with 0
# index means position 
#we can only access the characters by index but we can change them
str = "shagufi ali"
ch1 = str[0] #s
ch2 = str[1] #h
ch3 = str[7] #empty
print(ch1)
print(ch2)
print(ch3)

#Slicing, means accesing parts of str, here we write startingindex:endingindex, in output it doesn't include ending one
str = "shagufi ali"
print(str[2:6]) #aguf it includes 2 but not 6
print(str[0:7])
print(str[8:11]) #for getting last index , in endingindex we plus one or instead of that len(str) or just blank...
print(str[8:len(str)]) 
print(str[8:]) #means [8:len(str)]
print(str[:7]) #means [0:7]

#slicing also have negative index, last index is -1 then backward -2,-3...
print(str[-3:len(str)]) 

#str.functions
#str.endswith("") , it checks wheater our str ends with this substr or not, if yes it returns True
str = "My name is Shagufi ali"
print(str.endswith("li")) #True
print(str.endswith("sti")) #False

#str.capitalize(), it capitalize the 1st chr of str, it doesn't change our original str so it works only once bcz it creates new one with 1st capital chr
str = "my name is Shagufi ali"
print(str.capitalize()) #printing My name is Shagufi ali
print(str) #printing original one
str = str.capitalize() # here we modify the original one
print(str) 

#str.replce("old", "new") , it replca old value to new
str = "My name is Shagufi ali"
print(str.replace("a", "g")) #all 'a' in str replce with 'g'
print(str.replace("Shagufi", "Shagun")) # here substr also replaced

#str.find("word"), it returs index of first time occurance of this word
str = "My name is Shagufi ali name"
print(str.find("a")) #4
print(str.find("name")) #3, here we also search for a substr, it gives first time occurance index
print(str.find("p")) #here it doesnt exist in str so we get -1, here never thought of negative index, it simply means not exist

#str.count("word"), it counts no. of occurance
print(str.count("name")) #2
print(str.count("a")) #4
print(str.count("bababababa"))











