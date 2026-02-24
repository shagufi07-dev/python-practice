#user input validator analyzer

while True:
  username = input("username: ")
  if len(username) > 10:
    print("too long")
    continue
  elif len(username) < 3:
      print("too short")
      continue
  else:
      if username.islower():
          print("your username: ", username.capitalize())
          break
      else:
          print("your username: ", username) 
          break         


while True:
    age = int(input("age: "))
    if 15 <= age <= 100:
        print("Varified")
        break
    elif 0 <= age < 15:
        print("too young")
        continue
    else:
        print("unrealistic")
        continue
print("your age:", age)


while True:
    pin = input("Type 4 digit pin: ")

    if len(pin) > 4 or len(pin) < 4:
        print("Invalid")
        continue
    else:
        if len(set(pin)) < 4:
            print("Weak pin")
            continue
        else:
            print("Strong pin")
            break


numbers = []
i = 1
while i <= 5:
    numbers.append(int(input("num : ")))
    i += 1
numbers.sort()
print("Largest number: ",  numbers[-1])
print("Smaller number: ", numbers[0])

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
















