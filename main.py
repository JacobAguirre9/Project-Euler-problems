# These are my solutions to Project Euler problems! I hope they can be useful for you

# Problem 1- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# So, let's build a program that can compute this sum!

def sumcomputation():
    answer= sum(x for x in range(1000) if(x % 3==0 or x % 5==0))
    return str(answer)

if __name__== "__main__":
        print(sumcomputation())

# So, after running this function we find that the answer for the sum of all multiples of 3 or 5 below 1000, is equal to 233168!
# Thus, this answer is complete.