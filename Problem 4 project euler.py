# These are my solutions to Project Euler problems! I hope they can be useful for you

# Problem 4: Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Ok, so we'll need to first write a function that will compute the multiplication of two numbers, and then check to see if
# these two numbers, when multiplied, will produce a number that can be read the same from backwards to front.

def PalindromeProduct():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(ans)

# After running this code, we find that the answer is 906609
# Thus, this number is the largest Palindrome product that can be made from 2 three digit numbers.

# Hope this helps!

if __name__ == "__main__":
	print(PalindromeProduct())
