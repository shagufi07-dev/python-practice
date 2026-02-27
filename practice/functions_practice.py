#Question 1: WAF to print the length of a list. (list is the parameter)

cities = ["dehradun", "blr", "pune", "hyd"]
heros = ["ironman", "zoro", "spiderman"]
numbs = [3, 7, 9, 2, 0, 1, 5]

def calc_len(list):
    print(len(list))

calc_len(cities) #4
calc_len(heros) #3
calc_len(numbs) #7
  

#=======================================================


#Question 2: WAF to print the elements of a list in a single line. (list is the parameter)

heros = ["ironman", "zoro", "spiderman"]
numbs = [3, 7, 9, 2, 0, 1, 5]

def print_list(list):
    for el in list:
        print(el, end=" ")

print_list(heros)
print() # so both list don't print on same line
print_list(numbs)


#===========================================================


#Question 3: WAF to find the factorial of n.(n is the parameter)

def calc_fac(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    print("Factorial: ", fac)

calc_fac(int(input("n = ")))


#==========================================================


#Question 4: WAF to convert USD to INR

def conversion(usd_val):
    inr_val = usd_val * 90.97
    print(usd_val, "USD = ", inr_val, "INR")

conversion(float(input("usd_val= ")))


#===========================================================


#Question 5:WAF to give output that n is odd or even

def numb_nature(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")

numb_nature(int(input("n = ")))


#=======================================================

