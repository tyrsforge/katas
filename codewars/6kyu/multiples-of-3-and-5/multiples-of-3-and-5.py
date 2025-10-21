# Simple version

def solution(n):
	if n <= 0: return 0

	sum = 0

	for i in range(1, n):
		if i % 3 == 0 or i % 5 == 0:
			sum += i

	return sum

print(solution(10))

# Pythonic version

def pythonic_solution(n):
	return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)

print(pythonic_solution(10))


# By default, Python limits recursion depth to 1000 calls to prevent stack overflow.
# You can increase this limit with sys.setrecursionlimit(), but doing so may cause
# a crash if the recursion goes too deep because Python does not optimize tail calls.

def recursive_solution(n):
	if n <= 0: return 0

	return sum_multiples(n - 1)

def sum_multiples(n):
	if n == 0: return 0

	sum = n if n % 3 == 0 or n % 5 == 0 else 0

	return sum + sum_multiples(n - 1)

print(recursive_solution(998))
