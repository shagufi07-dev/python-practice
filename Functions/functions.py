#FUNCTIONS:helps to deacre redundency in code 

#function definition
def calc_sum(a, b): #(parameter1, parameter2,..)
    return a + b

sum = calc_sum(1, 2) #function call(argument1, argument2,..)
print(sum) #3


#a fn which has no parameter and no return 
def print_hello(): #we can left paramenthethisis empty as printing hello doesn't need any parameters
    print("hello")

print_hello()
print_hello()

output = print_hello()
print(output) #a fn which has no return so its giveS "NONE"



#fn to calculate avg of 3 numbs

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(1, 2, 3) #2


#built-in functions: like print(), type(), etc etc  
print("shagufi","ali") #sep = " "

print("shagufi")  #automatically end = "\n" (next line)
print("ali")

print("shagufi", end = " ") #now end =" " so they print on same line with space
print("ali")

print("shagufi", end = "$") #print on same line '$' in between them
print("ali")

#user defined function: those one which we gonna defined in our code

#default parameters, assigning a default value to parameter, which is used when no argument is passed.
def cal_product(a=1, b=3): #if we wanna store only 1 deafault val so it should be the last one
    print(a * b)
    return a * b

cal_product() #3


def cal_prod(b, a=2):
    print(a * b)
    return a * b

cal_prod(2) #4