#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:56:40 2017

@author: caitlinshener
"""
import matplotlib.pyplot as plt
#challenge 1 - happiness
"""
Takes in text. Then calculates 50 in each direction (or if the first word is 
less the fifty then it uses the first word, and same for the last word). Finds
happiness score for that set of 100 words. Increases by 20 to do the same. 
saves xvalues every 20 words. saves the associated y vales to a list. Graphs x 
and y values

"""

def happiness(words): 
    totalworth= 0
    fid = open('/Users/caitlinshener/Downloads/happiness_dictionary.txt', 'r') 
    worth=fid.read() 
    exec(worth) 
    for w in words: 
        for key in happiness_dictionary: 
            if key == w: 
                totalworth += happiness_dictionary[w]
#divided by 10 so it would be more nuanced
    totalworth = totalworth/ (len(words)*10)
    return totalworth

def storyarc(story): 
    story = story.lower()
    story=  story.split(' ')
    storylength= len(story)
    # a x-value every 20 words
    xvalues= range(0,storylength, 20)
     #text range will contain two values, the minimum and the maximum! 
    textrange= [0,0]
     #I will append all the y- values to this after I calculate them
    yvalues= []
    for x in xvalues: 
        #if it is less then 50. range is 0 to 50 past the number
        if x < 50: 
            textrange[0]=0
            textrange[1] = (x+49)
        #if closer to end then 50 
        elif ((storylength - x) <=  50):
            textrange[0] = (x -50) 
            textrange[1] = (storylength-1)
        else:
            textrange[0] = (x-50)
            textrange[1] = (x+49)
        yvalues.append(happiness(story[textrange[0]: textrange[1]]))
    # this part makes the graph 
    plt.plot(xvalues, yvalues,  'ro')
    plt.ylim(0, 1)
    plt.xlim(0, storylength)
    plt.ylabel('Happiness Score')
    plt.xlabel('Location in story')
    plt.title('The Happiness of a Story')
    plt.show()
    return
    
#connect one point to the next? More like a line? -- nope! not needed! 


araby = open('/Users/caitlinshener/Desktop/PIC10B/Pic10B_Hw5pt2/Pic10B_Hw5pt2/araby.txt', 'r')
arabystory = araby.read()
storyarc(arabystory)

#challenge 2 

"""
This takes in a np array with float values and returns the page rank of each 
node. 
"""

import numpy as np 

def pagerank(n):
# add teleportation constant p = .1 (the system has to be connected)
    p = .1 
    n= n + p
    numberofnodes= len(n[0,:])
#sum the columns. divide each element by the sum -- do this in a loop 
    for column in range(numberofnodes):
        total = np.sum(n[:,column])
        n[:,column] = n[:,column] / total
#find the eigvector eigvals
    eigvals,eigvecs=np.linalg.eig(n)
#next two lines find the eigenvector you want 
    b=abs(eigvals)
    e= np.where(b==max(b))[0][0]
#this calculates the probability  
    sum= np.sum(eigvecs[:,e])
    prob = (eigvecs[:, e])/ sum

# create new array that is the sorted version of your probability 
    sorted= np.sort(prob)
# create another list that is full of zeros  
    rank =  [0] * numberofnodes 
    scores = 1
    for f in range((numberofnodes -1), 0, -1):
        # use find function to find the n-1th element in the sorted array 
        place= np.where(prob == sorted[f])
# change prob at that place to be something different so that is cannot be found again for ties
# changed it to 0, so that would never be a max  
        placetwo= place[0][0]
        prob[placetwo]=0
        rank[placetwo]= scores
        scores += 1
    return rank

#challenge 3.
""" this calculates the degree of each node by summing up the values in 
a row and dividing by the total degrees. It finds the rank by
referencing the function above.
"""
#add up the number in each column 
def degree(m): 
    numberofcols= len(m[0,:])
#this will hold the degree of each node for now it is all zeros
    degrees = np.zeros(shape=(1, numberofcols))
#for loop calculates the degree of each node through adding
    for c in range(0,numberofcols): 
        temp= np.sum(m[:,c])
        degrees[0,c]= temp
#divide by total to make degree strength score
    total = np.sum(degrees)
    degrees = degrees /total
#we need to turn everything in degree into a list
    degrees2= degrees[0]
    degrees3= degrees2.tolist()
    pr= pagerank(m)
    return degrees3, pr



#challenge 5 

#taking a matrix to a power is the same as finding the number of paths of
#length k 

def number_paths(G,v,w,k): 
    mat =  np.linalg.matrix_power(G,k) 
    return mat[v,w]

G=[[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
v=0
w=3
k=20

print number_paths(G,v,w,k)