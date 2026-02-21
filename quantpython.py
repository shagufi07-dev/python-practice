
#Qestion1: SALARY RATIO SPLIT

total_salary = int(input("Enter total salary: "))
ratio_a = int(input("Enter A's share: "))
ratio_b = int(input("Enter B's share: "))
total_ratio = (ratio_a + ratio_b)

if(total_salary <= 0):
    print("Salary should be greater than 0!!")
elif(ratio_a <= 0 or ratio_b <= 0):
    print("Ratio should be positive!!")
elif(total_ratio == 0):
    print("INVALID ratios")
else:
    share_a = (total_salary*(ratio_a/total_ratio))
    share_b = (total_salary*(ratio_b/total_ratio))
    print("A's share: ", round(share_a, 2))
    print("B's share: ", round(share_b, 2))


#===============================================================


#Question 2: MILK WATER MIXTURE
import math
milk = int(input("Enter milk's quantity (L): ")) 
water = int(input("Enter water's quantity (L): "))

if(milk < 0 or water < 0):
    print("INVALID quantity")
elif(milk == 0 and water == 0):
    print("ratio: ", 0, ":", 0)
    print("milk_%: ", 0, "%")
    print("water_%: ", 0, "%")
else:
    g = math.gcd(milk,water)
    ratio_m = milk//g
    ratio_w = water//g
    print("ratio milk : water: ", ratio_m, ':', ratio_w)
    totalR = ratio_m + ratio_w
    milk_per = (ratio_m/totalR)*100
    water_per = (ratio_w/totalR)*100
    print("milk percentage in mixture: ", round(milk_per,2),"%")
    print("water percentage in mixture: ", round(water_per,2),"%")
    if(water_per > milk_per):
        if(milk_per == 0):
            print("PURE WATER!!")
        else:
            print("LOW QUALITY!!")
    elif(water_per < milk_per):
        if(water_per == 0):
            print("PURE MILK")
        else:
            print("GOOD QUALITY")
    else:
        print("MODERATE QUALITY")



#=================================================================


#Question 3: POCKET MONEY DISTRIBUTION 3:5:7

total_amount = int(input("Enter Total Amount: "))
ratios = [3,5,7]
total_ratio = sum(ratios)

if total_amount > 0:
    frnds_share = [total_amount*(ratios[0]/total_ratio), total_amount*(ratios[1]/total_ratio), total_amount*(ratios[2]/total_ratio)]
    print("1st friend share: ", frnds_share[0])
    print("2nd friend share: ", frnds_share[1])
    print("3rd friend share: ", frnds_share[2])
    print("Highest share:", max(frnds_share))
elif total_amount == 0:
    print("No money distribution")
else:
    print("INVALID amount!!")



