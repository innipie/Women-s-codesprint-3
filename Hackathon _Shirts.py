#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    sizes = map(int, raw_input().strip().split(' '))
    v = int(raw_input().strip())
    lis=[]
    for a1 in xrange(v):
        smallest,largest = raw_input().strip().split(' ')
        smallest,largest = [int(smallest),int(largest)]
        # your code goes here
        for i in range(smallest,largest+1):
            lis.append(i)
    c=0
    lis=set(lis)
    for s in sizes:
        if s in lis:
            c=c+1
    
    print c    
