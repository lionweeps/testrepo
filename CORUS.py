# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:19:53 2020

@author: z0045mjs
"""

def solve():
    x = [int(i) for i in input().split()]
    s = str(input())
    space = {}
    for j in s:     
        if j in space: 
            space[j] += 1
        else: 
            space[j] = 1

    for i in range(x[1]):
        c = int(input())
        wait = 0
        for k in space.keys():
            wait += max(0, space[k] - c)
        print(wait)
    

cas = int(input())

for i in range(cas):
    solve()
    
#def solve():
#    x = [int(i) for i in input().split()]
#    s = str(input())
#    for i in range(x[1]):
#        c = int(input())
#        space = {}
#        wait = 0
#        if c == 0:
#            wait = len(s)
#        else:    
#            for j in s:     
#                if j in space: 
#                    space[j] += 1
#                    if space[j] > c:
#                        wait += 1
#                else: 
#                    space[j] = 1
#
#        print(wait)
#    
#cas = int(input())
#
#for i in range(cas):
#    solve()
