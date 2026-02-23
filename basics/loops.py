#LOOPS, used to reapeat instructions

#while(condition):
#     some work,,   till the condition is 'TRUE' the 'WORK' happens on reapeat 
#we should add the stopping condition otherwise it creates infinite loop.

# write hello 5 times 
i = 1 # interator(the variable which we take here), iteration(means the process in which runs in loop with the help of iterator)
#first iteration means first round, second iteration means second round, and so on..
while i <= 5: 
    print("hello")
    i += 1 # it updates the i 
print(i) #prints the last i which it checks, here it is 6

#for 100 times 
i = 1 #initialization
while i <= 100:
    print("ZORO", i) #prints every i in the loop till last one which is 100
    i += 1
print(i) #prints only last checked i, which is 101 

#prints numbs 1 to 5
i = 1
while i <= 5:
    print(i) #1,2,3,4,5
    i += 1


#reverse 5 to 1
i = 5
while i >= 1:
    print(i) # 5,4,3,2,1
    i -= 1



##BREAK 
#wherever we used it in the loop, our loop terminates(stop) there.

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break #when it comes to 3 then loop breaks, never print till 5
    i += 1
print("end")


##CONTINUE

i = 0 
while i <= 5:
    if(i == 3): 
        i += 1  #when 3 comes it becomes 4 here
        continue #then this continue, starts the loop from while statement, it skips the statements comes after it and start loop again
    print(i)
    i += 1

#skip even numbs till 10

i = 1 
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1 



#for loop, used for sequential travel(travel by sequence). For traversing tup/list/str/etc..
#for variable in list/tup: ,,, here all elements store one by one in that variable
     #some work

numbs = [1, 2, 3, 4, 5]

for val in numbs:
    print(val) #printing all values in the list

fine_shyts = ("zoro", "draco", "tony", "harvey", "mike", "john", "robb")

for name in fine_shyts:
    print(name)

name = "Shagufi"

for chr in name:
    print(chr) #prints chr indivisually

#generally, if we wanna work on iterator than use while loop, if wanna traverse on a datatype then use for loop.

#we can use else here also.
#for el in list:
   #some work
#else: 
   #work when loop ends

name = "Shagufi"

for chr in name:
    if(chr == "g"):
        print("g found")
        break #here loop ends and never runs the else statement, as it runs only when loop fully runs
    print(chr)
else:
    print("end")


##range(),, range fn returns sequence of nums, starting from 0 by default(if not add start), and increase by 1 by default(if not add step), and stops before a numb(ending num is not included)
#range(start,stop,step) step means how much increment
print(range(5)) #printing range(0,5)

seq = range(5)
#we can print its elements by indexing
print(seq[0]) #0
print(seq[1]) #1


#print range elements indivisually by loop
for i in range(3, 10): #range(start, stop)
    print(i)

for i in range(2, 10, 2): #range(start, stop, step)
    print(i)


#print even numbs till 100
for i in range(2, 101, 2):
    print(i)
#odd nos.
for i in range(1, 100, 2):
    print(i)



#pass statement, pass is null st. that does nothing if we wanna complete  the loop in future
for i in  range(5):
    pass #if we don't use pass here so the after code doesn't run as our loop should have work first 

print("some useful work")



