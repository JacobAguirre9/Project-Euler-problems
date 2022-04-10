#Problem 3 Project Euler: Largest Prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Although this code is written only for the purpose of finding the prime factorization of this particular number
# it's important to recognize the usefulness and many applications that exist for finding the largest prime factor
# particularly in problems in analytic number theory or cryptography.

# I will state it here, as I will be using this library for many of my other solutions:
# I intend to use the popular "Eulerlib" package, as it has a library of recreational mathematics and number theory related functions
# for solving problems in Project Euler.

import eulerlib

def sumcompute():
	n = 600851475143
	while True:
		p = smallest_prime_factor(n)
		if p < n:
			n //= p
		else:
			return str(n)

# So, what does the code above do? We define n to be the number we're interested in.
# While this statement is true, we create another variable named p, and define this to be the smallest prime factor of (n).
# Then, we take the value 'n' and subsequently divide out its smallest factor(which is also prime) over multiple iterations, then the last
# factor that we divide out implies it must be the largest prime factor of parameter n.

def smallest_prime_factor(n):
	assert n >= 2
	for i in range(2, eulerlib.sqrt(n) + 1):
		if n % i == 0:
			return i
	return n

# Finally, we include the same bit of code from our last project here

if __name__ == "__main__":
	print(compute())