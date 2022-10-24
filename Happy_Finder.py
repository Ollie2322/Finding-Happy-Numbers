# -*- coding: utf-8 -*-
"""
A Python Programme that tests all the numbers in a range to test if they are happy. 
It then creates a file of all the happy numbers. 
"""

##############################################################################

def happy(number):
    a=number%10
    b=((number-a)%100)/10
    c=((number-(a+b))%1000)/100
    d=((number-(a+b+c))%10000)/1000
    e=((number-(a+b+c+d))%100000)/10000
    f=((number-(a+b+c+d+e))%1000000)/100000
    g=((number-(a+b+c+d+e+f))%10000000)/1000000
    h=((number-(a+b+c+d+e+f+g))%100000000)/10000000
    i=((number-(a+b+c+d+e+f+g+h))%100000000)/10000000
    j=((number-(a+b+c+d+e+f+g+h+i))%1000000000)/100000000

    return (a**2)+(b**2)+(c**2)+(d**2)+(e**2)+(f**2)+(g**2)+(h**2)+(i**2)+(j**2)
"""
The Above function uses modulo to seperate the number into it's didgits and then 
sums the square of the digits.  
"""
##############################################################################

tried_numbers=[]
happy_set=[]
not_happy=[]


for number in range(int(10e7)):
    original=number
    print original
    test=[]
    test.append(original)
    
    
    while number!=1:
        number=happy(number)
        if number in test:
            break
        else: 
            test.append(number)
            
            
    if number==1:
        for item in test:
            if item not in happy_set:
                happy_set.append(item)
            if item not in tried_numbers:
                tried_numbers.append(item)
                
            
    if number!=1:
        for item in test:
            if item not in not_happy:
                not_happy.append(item)
            if item not in tried_numbers:    
                tried_numbers.append(item)
                
happy_set.sort()

outfile=open("trial.txt","w")
for item in happy_set:
    outfile.write(" %10d \n" %(item))
outfile.close()
