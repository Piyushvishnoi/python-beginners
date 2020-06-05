weight = int(input("weight: "))
unit = input("kilo(K) or lbs(L): ")
if unit.upper() == "L":
    convertedweight = weight * 0.45
    print("Weight in kilo:" + str(convertedweight))
elif unit.upper() == "K":
    convertedweight = weight / 0.45
    print("Weight in lbs:" + str(convertedweight))    
else: 
    print("Unit entered is wrong")        
