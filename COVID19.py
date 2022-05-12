# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:57:26 2020

@author: z0045mjs
"""


def solve():
    n = int(input())
    x = [int(i) for i in input().split()]
    
    # start
    ans = 1
    covid = []
    for i in range(len(x)-1):
        if x[i+1] - x[i] <= 2:
            ans += 1
        else:
            covid.append(ans)
            ans = 1             
    covid.append(ans)
            
    # end
    print(min(covid),max(covid))


    
