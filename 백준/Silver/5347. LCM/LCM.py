import sys
input = sys.stdin.readline
n = int(input())

def gcd(a,b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

for _ in range(n):
    a,b = map(int,input().split())
    print(a*b//gcd(a,b))