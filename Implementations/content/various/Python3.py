/**
 * Description: Solution to CF Factorisation Collaboration. Demonstrates usage of Decimal.
 * Source: own
 * Verification: 
	* https://codeforces.com/contest/1091/problem/G
	* https://open.kattis.com/problems/catalansquare
 */

from math import *
import sys, random
def nextInt():
	return int(input())
def nextStrs():
	return input().split()
def nextInts():
	return list(map(int,nextStrs()))
 
n = nextInt()
v = [n]
def process(x):
	global v
	x = abs(x)
	V = []
	for t in v:
		g = gcd(t,x)
		if g != 1:
			V.append(g)
		if g != t:
			V.append(t//g)
	v = V
for i in range(50):
	x = random.randint(0,n-1)
	if gcd(x,n) != 1:
		process(x)
	else:
		sx = x*x%n # assert(gcd(sx,n) == 1)
		print(f"sqrt {sx}")
		sys.stdout.flush()
		X = nextInt()
		process(x+X)
		process(x-X)
print(f'! {len(v)}',end='')
for i in v:
	print(f' {i}',end='')
print()
sys.stdout.flush() # sys.exit(0) -> exit
# sys.setrecursionlimit(int(1e9)) -> stack size
# print(f'{ans:=.6f}') -> print ans to 6 decimal places

from decimal import * # arbitrary precision decimals

ctx = getcontext()
ctx.prec = 28
print(Decimal(1) / Decimal(7)) # 0.1428571428571428571428571429
print(ctx.power(Decimal(10),-30)) # 1E-30