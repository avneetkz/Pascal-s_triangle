# import factorial library from math module
from math import factorial

n= int(input("Enter number of rows for pascal's triangle: "))

# main for loop
for i in range(n+1):
    
    # for left spacing
    for j in range(n-i+1):
        print(end =' ')
     
    # for printing numbers
    for k in range(i+1):
        
        # nCr = n!/((n-r)!*r!)
        ele= factorial(i)/ factorial(k)* factorial(i-k)
        print(int(ele), end= ' ')

    # for new line
    print()
