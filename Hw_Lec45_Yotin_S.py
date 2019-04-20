inputRound = int(input("Please Enter Number : "))
Sum = 0
for x in range(inputRound):
    inputNumber = int(input('x'+str(x+1)+' = '))
    Sum = inputNumber + Sum
print('sum = ',Sum)
    
