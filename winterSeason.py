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
# def threeAndFive(myNum):
#     myNum -= 1
#     if myNum == 0:
#         return 0;
#     elif (myNum%3==0) or (myNum%5==0):
#         return myNum + threeAndFive(myNum)
#     else:
#         return threeAndFive(myNum)
#
#
# print(threeAndFive(999))


# Problem 2
#LOOP WAY
# def printFib(myNum):
#     myArr = [0,1,1]
#     if myNum < 0:
#         print("You can't use a negative number!")
#     elif myNum < 3:
#         return myArr[0:myNum]
#     else:
#         for i in range(3,myNum+1):
#             myArr.append(myArr[i-1] + myArr[i-2])
#     return myArr[1:]
#
# print(printFib(10))

def evenFibs(myNum):
    myArr = [1,2]
    runTot = 0
    i = 1
    while myArr[i] < myNum:
        if myArr[i]%2 == 0:
            runTot += myArr[i]
        else:
            runTot += 0
        i += 1
        myArr.append(myArr[i-1]+myArr[i-2])
    return runTot

print(evenFibs(4000000))
