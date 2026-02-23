#if-elif-else

#if(condition):
    #statement ,, this st. executes only when condition written in 'if' is 'True'

age = 22

if(age >= 18):
    print("Can vote") #indentation, means propeer spacinggggg
    print("can drive")

 #elif(condition):
     #statement, it executes when the 'if' condition 'not true', elif and if can use many times
light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"): #if one condition comes true then code ignores rest of the elifs 
    print("go")
elif(light == "yellow"): #ignoredddddd:)
    print("wait")

#code never ignore 'if' st. it everytime checks 'if', even one comes true
num = 6

if(num > 3):
    print("greter then 3")
if(num > 5):
    print("greter then 5") #here we get both st. bcz its 'if',  but if we use'elif' so code ignore if one gets true

#else use only once, and only at last, and we never give a conditionn to it bcz it only executes when the upper ones all wrong otherwise it doesn't execute

#elif:
    #statement

light = "pink"

if(light == "red"):   #false
    print("stop")
elif(light == "green"): #false
    print("go")
elif(light == "yellow"): #false
    print("wait")
else:
    print("light is BROKEN") #executes


#we can also use only if and else
age = 14

if(age >= 18):
    print("Can vote")
else:
    print("CANNOT vote")


#nesting, means we put one 'if' st. into another
age = int(input("Enter your age: "))

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")