# #Question 1: WAF to print the length of a list. (list is the parameter)

# cities = ["dehradun", "blr", "pune", "hyd"]
# heros = ["ironman", "zoro", "spiderman"]
# numbs = [3, 7, 9, 2, 0, 1, 5]

# def calc_len(list):
#     print(len(list))

# calc_len(cities) #4
# calc_len(heros) #3
# calc_len(numbs) #7
  

# #=======================================================


# #Question 2: WAF to print the elements of a list in a single line. (list is the parameter)

# heros = ["ironman", "zoro", "spiderman"]
# numbs = [3, 7, 9, 2, 0, 1, 5]

# def print_list(list):
#     for el in list:
#         print(el, end=" ")

# print_list(heros)
# print() # so both list don't print on same line
# print_list(numbs)


# #===========================================================


# #Question 3: WAF to find the factorial of n.(n is the parameter)

# def calc_fac(n):
#     fac = 1
#     for i in range(1, n+1):
#         fac *= i
#     print("Factorial: ", fac)

# calc_fac(int(input("n = ")))


# #==========================================================


# #Question 4: WAF to convert USD to INR

# def conversion(usd_val):
#     inr_val = usd_val * 90.97
#     print(usd_val, "USD = ", inr_val, "INR")

# conversion(float(input("usd_val= ")))


# #===========================================================


# #Question 5:WAF to give output that n is odd or even

# def numb_nature(n):
#     if n%2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")

# numb_nature(int(input("n = ")))


#=======================================================

#Ouestion 6: WAF to check nature of numb, odd or even

# def num_nature(n):
#     if n%2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"
    
# result = num_nature(int(input("n: ")))
# print(result)


#=========================================================

#Question 7: Absolute dfference of two numbes

# def abss_diff(a, b):
#     diff = a - b
#     if diff < 0:
#         diff = -diff
#     return diff
        
# a = int(input("a : "))
# b = int(input("b : "))

# result = abss_diff(a,b)
# print(result) 


#=================================================================

#Question 8:

# def numb_nature(n):
#     if n == 0:
#         nature = "Zero"
#     elif n > 0:
#         if n%2 == 0:
#             nature = "Positive Even"
#         else:
#             nature = "Positive Odd"
#     else:
#         if n%2 == 0:
#             nature = "Negative Even"
#         else:
#             nature= "Negative Odd"
#     return nature 
 
# result = numb_nature(int(input("n : ")))

# print(result)


#=============================================================

#Question 9: calculate SI and amount

# def calc_interest(P, R, T):
#     I = (P*R*T)/100
#     return I

# def calc_amount(P , I):
#     return P + I

# P = float(input("Principal : "))
# R = float(input("Rate : "))
# T = float(input("Time (in years) : "))

# interest = calc_interest(P,R,T)
# amount = calc_amount(P,interest)

# print(interest,"\n",amount)


#===============================================================

#Question 10:

# def find_max(a, b, c):
#     return max(a, b, c)

# a = int(input("a : "))
# b = int(input("b : "))
# c = int(input("c : "))

# max_number = find_max(a, b, c)
# print(max_number)


#e===========================================================

#Question 11:

# list1 = [1, 7, 4, 2, 9, 10, 28]
# list2 = [8, 9, 2, 5, 7, 20, 23]


# def calc_sum(list_par):
#     total = 0
#     for el in list_par:
#         total += el

#     return total


# a = calc_sum(list1)
# print(a)
# b = calc_sum(list2)
# print(b)


#============================================================

#Quesrion 12: 

numb = [6,3,2,9,8,6,1,0]


def find_second_largest(list_par):
    highest = -1
    second_highest = -1
    for el in list_par:
        if el > highest :
            highest = el
    return highest

x = find_second_largest(numb)
print(x)