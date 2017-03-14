
import sys


n = int(raw_input().strip())
squares = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]
# your code goes here
c=0
for i in range(n):
    if d==sum(squares[i:i+m]):
        c=c+1
print c
