#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:42:35 2017
Homework Assignment #3 for Applications in Python. 
@author: caitlinshener
"""



#challenge 1 PART ONE -- SCATTER PLOT 
import matplotlib.pyplot as plt




plt.ylabel('Number of Male Soccer Concussions')
plt.xlabel('Number of Female Soccer Concussions')
plt.title('Soccer and Lacrosse Concussions for Men and Women Between 1997 to 1999')
Female = [51, 47, 60, 12,7,7]
Male = [34, 27, 40, 19, 15, 17]
plt.plot(Female, Male,  'ro')
plt.ylim(5, 70)
plt.xlim(5, 70)
plt.show()

concussions = [51,47, 60, 12, 7, 7, 16, 30, 26, 9, 10, 28, 1, 0, 0, 34, 27, 40, 19, 15, 17, 8, 21, 20, 22, 6, 25, 0,0,0]	
plt.hist(concussions)
plt.title("Histogram of Number of Concussions For Each Year and Sport")
plt.xlabel("Number of Concussions")
plt.ylabel("Frequency")
plt.show()

#challenge 2
#Visualize a small network of your own choosing in a helpful way. This means that you may use labels, directed edges, colors, etc..., if they are appropriate to help interpret the data.#

"""
Jaemmie Canas	Anthropology
Cynthia Cervantes	Psychobiology
Wanarsa Tanie Chantara	Human Bio/Soc BA
Isabella Cordova	Psychology
Rachel Davis	Linguistics & Psychology
Alyssa Delagnes	Pscyhology
Emily Eliasof	Gender Studies
"""

people = [1,1,1,1,1,1,1]
majors= [3,3,3,3,3,3]
Ym = [1.5,2.5,3.5,4.5, 5.5, 6.5] 
Yp = [1,2,3,4,5,6,7] 

# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=10)

plt.xlim(0.0,4.3)
plt.ylim(0,8.3)
plt.scatter(people, Yp, color= "green")
plt.scatter(majors, Ym,  color= "green")


plt.legend(loc='upper left', frameon=False)

plt.annotate(r'Jaemmie', xy=(1, 1), fontsize=14) 
plt.annotate(r'Cynthia ', xy=(1, 2), fontsize=14) 
plt.annotate(r'Wanarsa', xy=(1, 3), fontsize=14) 
plt.annotate(r'Isabella ', xy=(1, 4), fontsize=14)
plt.annotate(r'Rachel', xy=(1, 5), fontsize=14)  
plt.annotate(r'Emily', xy=(1, 6), fontsize=14)  
plt.annotate(r'Alyssa', xy=(1, 7), fontsize=14)

majors = ["Anthropology", "Psychobiology", "Human Bio/Soc BA", "Linguistics"	,"Gender Studies", "Psychology" ] 

for r in range(6): 
    plt.annotate(majors[r], xy=(3, r+1.5), fontsize=14) 

plt.plot([1,3] ,[2,2.5], '-', color= "blue")
plt.plot([1,3] ,[1,1.5], '-', color= "blue")
plt.plot([1,3] ,[3,3.5], '-', color= "blue")
plt.plot([1,3] ,[4,6.5], '-', color= "blue")
plt.plot([1,3] ,[5,6.5], '-', color= "blue")
plt.plot([1,3] ,[5,4.5], '-', color= "blue")
plt.plot([1,3] ,[7,6.5], '-', color= "blue")
plt.plot([1,3] ,[6,5.5], '-', color= "blue")

plt.title('UCLA Disability Studies Minors and Their Majors',fontsize=18 )

plt.show()
#np.matrix([1,0],[0,1])

#challenge 3 - use turtle to make a fractal 
import turtle as t


def makesquare(n): 
    t.fd(n)
    t.left(90)
    t.fd(n)
    t.left(90)
    t.fd(n)
    t.left(90)
    t.fd(n)
def makefoursquare(n): 
    for i in range(4):
        makesquare(n)
    
colors = [ 'Light Pink', 'Pale Violet Red',	'Maroon', 'Medium Violet Red',	 	 
'Violet','Plum',	'Orchid', 'Medium Orchid', 'Dark Orchid','Dark Violet', 
'Blue Violet','Purple','Medium Purple','Thistle','Hot Pink',	'Deep Pink', 'Pink', 'Light Pink'	, 	 
'Pale Violet Red','Maroon',	'Medium Violet Red', 'Violet',	 
'Plum', 'Orchid'] 

n= 300
color = 0
while n> 5:
    t.color(colors[color])
   
    makefoursquare(n)
    n= n/2   
    t.fd(n)
    t.left(90)
    t.fd(n)
    t.right(90)
    color += 2
makefoursquare(n)  



#challenge 4: Use imshow/matshow in matplotlib to 
#create a 256 × 128 image that uses all 15-bit colors.

import numpy as np 


red = range(32)
green = range(32)
blue = range (32)
colorstest322 = np.zeros(shape=(256,128,3))
row= 1
matrix = 1
for r in range(32): 
    for g in range(32): 
        for b in range(32): 
            color= 0
            colorstest322[matrix-1, row-1, color] = red[r]/31.0
            color= 1
            colorstest322[matrix-1, row-1, color] = green[g]/31.0
            color =2
            colorstest322[matrix-1, row-1, color] = blue[b]/31.0
            row += 1
            if row > 128: 
                row = 0 
                matrix += 1                      
plt.imshow(colorstest322)
print len(colorstest322)

