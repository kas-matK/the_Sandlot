# Problem 1
# LOOP WAY
# def threeAndFive(myNum):
#     runTot = 0
#     for i in range(1,myNum):
#         if (i%3==0) or (i%5==0):
#             runTot += i
#         else:
#             runTot += 0
#     return runTot

# RECURSION WAY
# DO NOT USE a myNum ABOVE 999
def threeAndFive(myNum):
    myNum -= 1
    if myNum == 0:
        return 0;
    elif (myNum%3==0) or (myNum%5==0):
        return myNum + threeAndFive(myNum)
    else:
        return threeAndFive(myNum)


print(threeAndFive(999))
