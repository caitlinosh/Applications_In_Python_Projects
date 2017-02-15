#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:36:25 2017

@author: caitlinshener

"""

#Challenge 1 balance(eq)
"""
instructions: 
    
Write a function that takes an unbalanced chemical reaction and balances it. For example, the input
“C6H5COOH + O2 = CO2 + H2O” should give output “C6H5COOH + 15O2 = 14CO2 + 6H2O”.

notes: 
First I use a series of string splitting to find all the elements and compunds. 
Then, I made a matrix out of this information. Elements represented by rows and 
compounds represented by columns. I imput the numbers for elements and compounds 
into the matrix. Then I solve the matrix. After, I subtitute 1 for free varaibles, 
and solve for non- free varaibles. Then I multiply by LCD to get rid of fractions.
Lastly, I format the answer in a string to look like a balanced equation. 
"""

#challange 1: 
import re
import sympy as sp



def balance(equation):
#this finds all the elements 
    elements = []
    test= re.findall(r'[A-Z][a-z]*', equation)
    for i in range(0, len(test)):
        element= test[i]
        if element not in elements: 
            elements.append(element)
#next we need to find all the compounds

#find the leftside and right sides

    equations= equation.split('=')
    leftside= equations[0]
    rightside= equations[1]
#find leftside compounds and rightside compounds
    leftcompounds =  leftside.split('+')
    rightcompounds = rightside.split('+')


    numberofcompounds = len(leftcompounds) + len(rightcompounds)



#each element gets a row
#each compound gets a column and one extra 

    matrix = zeros( len(elements), (numberofcompounds))
# left compounds
    for l in range(0, len(leftcompounds)): 
        currentcompound= leftcompounds[l]
    
        for e in range(0, len(elements)): 
    #go through leftside compounds and add up the number of that element 
    #assume 1 or get the number after currentcompound= leftsidecompound
            temp=  currentcompound.split(elements[e])
            digits= []
            for t in range(0,len(temp)):
                match= re.search(r'^[0-9]+', temp[t])
        #0 digits unless it is replaced
                digit= 0
                if match:
                    digit=match.group()
                    cdigit= int(digit)
                    digits.append(cdigit)
            ones= len(temp)- len(digits)-1
            total= sum(digits) + ones
    #add total to matrix in the spot (e,l)
            matrix[e,l]= total

# right compounds- some thing just adding negitive numbers
    for l in range(0, len(rightcompounds)): 
        currentcompound= rightcompounds[l]
    
        for e in range(0, len(elements)): 
    #go through leftside compounds and add up the number of that element 
    #assume 1 or get the number after icurrentcompound= leftsidecompound
            temp=  currentcompound.split(elements[e])
            digits= []
            for t in range(0,len(temp)):
                match= re.search(r'^[0-9]+', temp[t])
        #0 digits unless it is replaced
                digit= 0
                if match:
                    digit=match.group()
                    cdigit= int(digit)
                    digits.append(cdigit)
                ones= len(temp)- len(digits)-1
            total= sum(digits) + ones
    #add total to matrix in the spot (e,l)
            matrix[(e,(l+ len(leftcompounds)))]= -total 

# creatint symbols to solve this matrix. 

    [X0, X1, X2, X3] = sp.symbols('X0:4')
    vars= [X0, X1, X2, X3]
#c= zeros(len(elements),1)
    variables = sp.Matrix([[X0], [X1], [X2], [X3]])
#solve the equations
    b = matrix*variables
    soln = sp.solve(b)
#note which variables are free or not by inn and notinn lists and innorout a bool list 
    notin= []
    inn= []
    innorout= []
# if a variable is not in the solution then it is notin 
# else it is inn

    for v in vars: 
        if v not in soln: 
            notin.append(v)
            innorout.append(0)
        else: 
            inn.append(v)
            innorout.append(1)
#now I am making a list of the solutions 
#if it is a free variable, it gets 1 
# if it is not a free variable, I solve for it using free varaibles = 1
    solutions= []
    count=0
    for i in innorout: 
        if i== 0: 
            solutions.append(1)
#solving for non- free varaibles 
        if i==1: 
            equation= soln[inn[count]]
            for n in notin: 
                equation= equation.subs(n,1)
            solutions.append(equation)
            count += 1
# finding lcd for fractions 

#list of things I will need to find the least common multiple of   
    lcms= []
#find fractions. save denominators
    for s in solutions: 
        fractest= fraction(s)
        if fractest[1] != 1: 
            lcms.append(fractest[1])
#find the lcm of the denominators 

    leastcommon= lcm(lcms)
#multiply everything by the lcd

    for s in range(0,len(solutions)): 
        solutions[s]= solutions[s]*leastcommon

# the rest of this is just formating the output in a string! 
    count= 0 
    balancedeq= ''
    for c in leftcompounds: 
        balancedeq = balancedeq + str(solutions[count]) + c
        if c != leftcompounds[len(leftcompounds)-1]: 
            balancedeq = balancedeq + '+' 
        count +=1

    balancedeq = balancedeq + '=' 

    for c in rightcompounds: 
        balancedeq = balancedeq + str(solutions[count]) + c
        if c != rightcompounds[len(rightcompounds)-1]: 
            balancedeq = balancedeq + '+' 
        count +=1
    
    return balancedeq

equation= 'CuBr2 + AlCl3 = CuCl2 + AlBr3'

print(balance(equation))

#Challenge 2: text encipher(s,pub key) 
"""
instructions: 
Write functions that encrypt and decrypt a word
 (string of capital letters) using the RSA method.
 
notes: 
text_encipher:
I created two dictionaries, map and unmap. I used map to go from letter to number. 
Then I enciphered the number. Then I used unmap to go from the enciphered number 
to letter. 
text_decipher: 
I used the same dictionaries as before. I first used map to go from letter to number. 
Then I deciphered the number. Then I used unmap to got from the deciphered number 
to letter. 

"""

from sympy.crypto.crypto import decipher_rsa, rsa_private_key, rsa_public_key, encipher_rsa



def text_encipher(s,pubkey): 
    #wasn't working for O, so I changed O to 27 and then it worked 
    map= {'A':1, 'B':2, 'C':3, 'D': 4, 'E':5, 'F': 6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
     'L':12, 'M':13, 'N':14,'O':27, 'P':16, 'Q':17, 'R': 18, 'S':19, 'T':20, 
     'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26} 
    letterscoded= []
    for w in s: 
        lettercode=map[w] 
        coded= encipher_rsa(lettercode, pubkey)
        letterscoded.append(coded)
    unmap=  {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K',
     12:'L', 13:'M', 14:'N', 27:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 
     21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26: 'Z'} 
    codedword= ''
    for l in letterscoded: 
         letter= unmap[l]    
         codedword = codedword + letter
    return codedword

p = 5
q= 7
e= 19

privkey = rsa_private_key(p, q, e)
pubkey = rsa_public_key(p, q, e)
s= 'PYTHON'  
t= text_encipher(s,pubkey)
print t

def text_decipher(t,privkey): 
    map= {'A':1, 'B':2, 'C':3, 'D': 4, 'E':5, 'F': 6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
     'L':12, 'M':13, 'N':14,'O':27, 'P':16, 'Q':17, 'R': 18, 'S':19, 'T':20, 
     'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26} 
    unmap=  {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K',
     12:'L', 13:'M', 14:'N', 27:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 
     21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26: 'Z'} 
    uncodednums= []
    for w in t: 
        numbercode= map[w] 
        decodednum= decipher_rsa(numbercode, privkey)
        uncodednums.append(decodednum)
    codedword= ''
    for l in uncodednums: 
         letter= unmap[l]    
         codedword = codedword + letter
    return codedword 

print text_decipher(t,privkey)



"""
Challenge 3 taylor figure(k)
Problem: Write a function that plots cos(x), and the Taylor expansions around
 x = 0 using the first 1, 2, . . . , k terms (k approximation
 functions in total). Choose an appropriate color scheme that 
 shows the in- creasing precision.
 
 notes: 
 First term is condsidered to be sign*(x**2) / sp.factorial(2)
 I only considered terms 1-12 because 12 looks like an exact 
 match for the scope of my graph, so it was not necissary to 
 continue to higher numbers. The function accepts k 1 to 12. 
 precision goes from red to green to blue. 
 
"""

import sympy as sp

def taylor_figure(k):
#cosine 
    x=sp.Symbol('x')
    expr= sp.cos(x)
#p1= sp.plot(expr)
# taylor expansion
#could have also used this function cos(x).series(x, 0, k)
    taylorexpr = 1 
    sign= -1
    power= 2
    colors= [ (1,0 ,0), (.85, .15,0), (.75, .25,0), (.5, .5, 0),(.25, .75,0), (.15, .85, 0), (0, 1,0), (0, .85, .15), (0, .75, .25),(0, .5, .5),(0, .25, .75), (0, .15, .85), (0, 0,1) ]
    color= colors[k-1]
    for i in range(1,k+1): 
        temp= sign*(x**power) / sp.factorial(power)
        taylorexpr = taylorexpr + temp
        power += 2
        sign *=(-1)
#So user can see the function 
    print (taylorexpr)
    p1= sp.plot(expr, ylim=(-10, 10), show=False, line_color='black' )
    p2= sp.plot(taylorexpr, ylim=(-10, 10), show=False, line_color= color)
# Make the second one a part of the first one.
    p1.extend(p2)
# Display the modified plot object.
    p1.show()
    return 
    

taylor_figure(3)
taylor_figure(7)


"""
Challenge 4 all_ sat(expr)
Write a function that works like the satisfiable function in sympy.logic.in 
reference, except that it returns all possible satisfying assignments,
for an expression in terms of two variables x, y.

notes: 
    I am only making this work for variables x and y- not other varaibles. I 
    tested each combination, and if it worked, I appened it to a list. """


def all_sat(expr):
    combinations= []
    if (expr.subs({x: True, y: True})== True): 
        combinations.append('X is TRUE and Y is TRUE')
    if (expr.subs({x: True, y: False})== True): 
        combinations.append('X is TRUE and Y is FALSE')
    if (expr.subs({x: False, y: True})== True): 
        combinations.append('X is FALSE and Y is TRUE')
    if (expr.subs({x: False, y: False})== True): 
        combinations.append('X is FALSE and Y is FALSE')
    if len(combinations) == 0: 
        combinations.append('No combinations work for this expression')
    return combinations

x=sp.Symbol('x')
y=sp.Symbol('y')


a=(x|y)&(~x|~y)
print all_sat(a)
    

