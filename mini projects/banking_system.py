print("REGISTRATION")

first_name = input("First name: ")
last_name = input("Last name: ")
name = first_name.capitalize() + " " + last_name.capitalize()

print(name)
while True:
  username = input("create username: ")
  if len(username) > 10:
    print("too long")
    continue
  elif len(username) < 3:
      print("too short")
      continue
  else:
     print("your username: ", username.lower())
     break       

while True:
    age = int(input("age: "))
    if 18 <= age <= 100:
        print("Varified")
        break
    elif 0 <= age < 18:
        print("too young")
        continue
    else:
        print("unrealistic")
        continue

while True:
    pin = input("Enter 4 digit pin: ")

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


while True:
    phone_no = input("Enter phone number: ")
    if phone_no.isdigit() and len(phone_no) == 10:
        break
    else:
        print("unrealistic phone number!!")
        continue

while True:
    email = input("Your Email: ")
    if 15 <= len(email) <= 20 and email.endswith("@gmail.com"):
        break
    else:
        print("check your email again!!")
        continue
print("Registration sucessful.")
acc_numb = 22331100229
print("Your account number : ", acc_numb)


while True:
    initial_dep = int(input("Initial Deposit(minimum amount 1000): "))  
    if 0 <= initial_dep < 1000:
        print("Initial deposit should be minimum 1000!!")
        continue
    elif initial_dep < 0:
        print('Unrealistic Amount!!')
        continue
    else:
        print("Amount deposited sucessfully.")
        account_balance = initial_dep
        break

bank = {
    "username" : username,
    "name" : name,
    "age" : age, 
    "pin" : pin,
    "phone_numb" : phone_no,
    "email" : email,
    "acc_numb" : acc_numb,
    "account_balance" : account_balance
}

print("LOGIN")

i = 1
while i <= 3:
    login_username = input("Enter username: ")
    login_pin = input("Enter pin: ")

    if login_username != bank["username"]:
     print("username not found")
     i += 1
     continue

    if login_pin != bank["pin"]:
        print("Incorrect pin!!")
        i += 1
        continue
    else:
         print("Sucessfully logined")
         break
    

while True:
    consent = input("can we help you (yes/no):")
    if consent.lower() == "yes":
        service = input("-Check Balance" "\n" "-Deposite Money" "\n" "-Withdraw Money" "\n" "-View Account Details" "\n" "-Change PIN" "\n" "-Logout" "\n" "Enter Here: ")
        service = service.lower()

        if service == "deposite money":
            while True:
                deposite =  int(input("Enter amount here : "))
                if deposite < 0:
                    print("unrealistic amount!!")
                    continue
                else:
                    print("Deposited sucessfully.")
                    bank["account_balance"] += deposite
                    break
            continue
        if service == "withdraw money":
            while True:
                withdraw = int(input("Enter amount here : "))
                if withdraw < 0:
                    print("unrealistic amount!!")
                    continue
                elif withdraw > account_balance:
                    print("Insufficient balance!!")
                    continue
                else:
                    print("successfully withdrawl.")
                    bank["account_balance"] -= withdraw
                    break
            continue
        if service == "change pin":
            i = 1
            while i <= 3:
                old_pin = input("old pin : ")
                if old_pin != bank["pin"]:
                    print("old pin doesn't match!!")
                    i += 1
                    continue
                else:
                    old_pin == bank["pin"]
                    new_pin = input("New PIN : ")
                    bank["pin"] = new_pin
                    break
            continue
        if service == "check balance":
            print(bank["account_balance"])
            continue
        if service == "view account details":
            filtered = {}
            for k, v in bank.items():
                if k != "pin":
                    filtered[k] = v
            for k,v in filtered.items():
                    print(k, ":", v)
            continue        
        if service == "logout":
            print('Sucessfully logged out.')
            break
    else:
        print("AS ur wish")
    break
                
         
   
    
    




    
