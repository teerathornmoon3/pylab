round = int(input("Enter round: "))
Result = 0

for i in range(round):
    Number = int(input("Enter number %d: " %(i+1)))
    Result += Number
    
print("Result :",Result)