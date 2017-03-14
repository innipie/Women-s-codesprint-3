#!/bin/python

import sys


r,c = raw_input().strip().split(' ')
r,c = [int(r),int(c)]
# your code goes here
s=""
for i in range(c):
	s +="..O.."
s +="\n"
for x in range(c):
	s +="O.o.O"
s +="\n"
for x in range(c):
	s+="..O.."
for i in range(r):
	print s
