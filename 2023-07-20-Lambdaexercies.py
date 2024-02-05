"""LAMBDA EXPRESSIONS PRACTICE"""



#to print a number after 15 is added
fifteen = lambda num : print(num+15)
fifteen(10)
#to print the product of 2 numbers
multiply = lambda x,y : print(x*y)
multiply(10,5)

#to find the max and min from this list of tuples
myList = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
maxNum =0
minNum = 0
for x,y in myList:
    if y > maxNum:
        maxNum = y
    elif y < minNum:
        minNum = y
    else:
        pass


