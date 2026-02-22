#user input validator analyzer

username = input("Type username: ")

if(3 <= len(username) <= 10):
    if(username.islower()):
        print("Your username: ", username.capitalize())
        print("Varified....Continue")
    else:
        print("Your username: ", username)
elif(len(username) > 10):
    print("Too long")
else:
    print("Too short") 

age = int(input("Type your age: "))

if(15 <= age <= 100):
    print("acceptable...continue")
elif(age < 15):
    print("too young")
else:
    print("unrealistic")

email = input("Enter your email: ")

if(10 <= len(email) <= 15):
    if(email.find("@") != -1 and email.find(".") != -1):
        print("Valid email...Continue")
        print("Now enter your 5 Fav numbers")
    else:
        print("Not valid")
elif(len(email) > 15):
    print("Too long")
else:
    print("too short")

numbers = []
numbers.append(int(input("num1: ")))
numbers.append(int(input("num2: ")))
numbers.append(int(input("num3: ")))
numbers.append(int(input("num4: ")))
numbers.append(int(input("num5: ")))
numbers.sort()
print("Largest number: ",  numbers[-1])
print("Shortest number: ", numbers[0])

if(numbers[-1]%2 == 0):
    print("Largest number is EVEN")
else:
    print("Laregst number is ODD")

slic1 = numbers[ : 2]
slic2 = numbers[2 : ]
print(sum(slic1))
print(sum(slic2))

if(sum(slic1) == sum(slic2)):
    print("slices sums are EQUAL")
elif(sum(slic1) > sum(slic2)):
    print("slice1 sum is GREATER")
else:
    print("Slice2 sum is GREATER")

pin = input("Type 4 digits PIN: ")
pin = (pin[0], pin[1], pin[2], pin[3])

if(pin.count(pin[0]) > 1 or pin.count(pin[1]) > 1 or pin.count(pin[2]) > 1 or pin.count(pin[3]) > 1):
    print("there is repeatetive numbers in PIN")
    print("Your PIN is WEAK")
    print("REJECTED")
else:
    print("Your pin is STRONG")
    print("WELCOME!!!!")















