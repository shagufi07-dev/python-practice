#Question 1: print numb 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1


#==============================================


#Question 2: print numb 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1 


#====================================================


#Question 3: print the multiplication table of numb n
n = int(input("n: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1


#==========================================================
  

#Question 4: print the elements of list
numb = [1,4,9,16,25,36,49,64,81,100]
# here we traverse, means when we travel at each element of list/tupple one by one.
idx = 0
while idx < len(numb): # < len(list) bcz last index is not equal to len(list) it is 1 less than it
   print(numb[idx]) #num[0], numb[1],...so on
   idx += 1

fine_shyts = ["zoro", "draco", "harvey", "tom riddle", "sanji"]

idx = 0
while idx < len(fine_shyts):
   print(fine_shyts[idx])
   idx += 1


#==================================================================


#Question 5: Search for a nmb x in tuple using loop
numb = (1,4,9,16,25,36,49,64,81,100,25)

x = int(input("x = "))

idx = 0 
while idx < len(numb):
    if(numb[idx] == x):
        print("FOUND at indx ", idx )
    else:
        print("finding")
    idx += 1
     #even after finding it isn't stop, it continues finding till last element of tup/list

#-------------------------------------------------
numb = (1,4,9,16,25,36,49,64,81,100,25)

x = int(input("x = "))

idx = 0 
while idx <= len(numb):
    if(numb[idx] == x):
          print("FOUND at indx ", idx )
          break #now it stops the loop when the x found
    else:
         print("finding...")
    idx += 1
print("end")


#====================================================================


#Quetion 6: print element of list by using for loop
numb = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in numb:
    print(val)


#======================================================================


#Question 7: search for x in tupple by using for loop 
# it is known as linear search when we search something in a tuple/list/etc
numb = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36]

x = int(input("x = "))

idx = 0
for val in numb:
    if (val == x):
        print("FOUND at indx", idx)
        break #so it found the numb once even if it exist more times
    idx += 1


#============================================================================


#Question 8: print nums 1 to 100 by for and range()
for i in range(1, 101):
    print(i)


#==========================================================================


#9 print nums from 100 to 1 by for and range()
for i in range(100, 0, -1): #step can be negative also
    print(i)


#==================================================================


#Question 10: print multiplication table of n
n = int(input("n = "))

for i in range(n , (n*10 + 1 ), n ):
    print(i)

#OR

n = int(input("n = "))

for i in range(1, 11):
    print(n * i)


#===============================================================


#Question 11: find sum of first n natural nums using while loop

n = int(input("n = "))
sum = 0
i = 1 

while i <= n:
    sum += i
    i += 1

print("total sum: " , sum)


#===============================================================


#Question 12: find the factorial of first n numbers using for loop
n = int(input("n = "))
fac = 1

for i in range(1, n+1):
    fac *= i 
print("factorial: ", fac)
