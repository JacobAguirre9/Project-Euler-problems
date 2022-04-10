# These are my solutions to Project Euler problems! I hope they can be useful for you

# This is truly one of the best problems linked on Project Euler.
# Often times, while grading PSets or reviewing someone's work, it's often the small algebraic errors they make and not the
# actual overhead theory. This problem seeks to look at problems with fractions

# Problem 33 Digit cancelling fractions

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
# believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# Solution begin: Alright so, we want to consider any arbitrary fraction in the form of n/d:
# As stated in the problem, we need 10 <= n < d < 100.

# The case of n0 = d0 is impossible due to the following reasons:
# Consider the following algebraic proof:
    #   n1 / d1 = n / d = (10*n1 + n0) / (10*d1 + n0).
    #   n1 * (10*d1 + n0) = d1 * (10*n1 + n0).
    #   10*n1*d1 + n1*n0 = 10*d1*n1 + d1*n0.
    #   n1*n0 = d1*n0.
    #   n1 = d1.
    #   This implies n = d, which contradicts the fact that n < d.
    # Q.E.D.

# Therefore, we cannot have the case of n1=d1 for the same reason.
# We only consider cases of n0 = d1 or n1 = d0.
# First case: consider that n1/d0 = n/d;
# Second case: Check if n0/d1 = n/d.

#Let's import the library of math, from which we'll use the "Greatest Common Denominator" tool

import math
def FractionComputation():
    numerator = 1
    denominator = 1
    for d in range(10, 100):
            for n in range(10, d):
                    n0 = n % 10
                    n1 = n // 10
                    d0 = d % 10
                    d1 = d // 10
                    if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                            numerator *= n
                            denominator *= d
    return str(denominator // math.gcd(numerator, denominator))


if __name__ == "__main__":
    print(FractionComputation())




