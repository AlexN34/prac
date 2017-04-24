mealCost = float(input())
tip = float(input())/100
tax = float(input())/100

totalCost = round((1 + tip + tax) * mealCost, 0)

print ("The total meal cost is %0d dollars." % ((totalCost)))