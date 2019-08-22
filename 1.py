def countCurrency(amount):
    notes = [2000,500,100,50,20,10] 
    noteCounter = [0,0,0,0,0,0]
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i 
            amount = amount - j * i 
            print (i ," : ", j)
amount = 2510;
countCurrency(amount)
