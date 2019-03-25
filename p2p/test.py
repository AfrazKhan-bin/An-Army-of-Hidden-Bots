with open("Transactions.txt",'r') as f:
    lisOfTransactions = f.read()
    if (len(lisOfTransactions) != 0 ):
        lisOfTransactions = lisOfTransactions.splitlines()
        lisOfTransactions = lisOfTransactions[-2]
        digit1 = int(lisOfTransactions[0])
        digit2 = lisOfTransactions[1]
        if (digit2 != '.'):
            number = int(str(digit1) + str(digit2))
        else:
            number = digit1
        number += 1
    else:
        number = 1

print (number)