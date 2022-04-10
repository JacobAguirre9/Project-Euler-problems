# These are my solutions to Project Euler problems! I hope they can be useful for you

# This is actually one of my favourite solutions I've written. I love applications of mathematics to graph theory, and in my own research
# this problem comes up often. I also love how this problem is sort of like a game, which i love. I hope you are able to find some usage out of this solution! :D

# Problem 18: Maximum Path Sum I


# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#     3
#    7 4
#   2 4 6
#  8 5 9 3

# So, the optimal path here in this triangle is 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:
# If you are curious as to what the actual triangle is, please visit https://projecteuler.net/problem=18

# Let's begin the solution!



def TriangleCompute():
	for i in reversed(range(len(triangle) - 1)):
		for j in range(len(triangle[i])):
			triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
	return str(triangle[0][0])

# What did this function above do? Well, We make a fresh empty triangle with the same measurements as the huge triangle we started with.
# We analyze each sub-triangle whose top is at each cell of the main triangle,
# compute the maximum path sum when beginning from this position, and save the result in the corresponding blank triangle cell.

triangle = [
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]

# The dependent values are almost always generated before they are used since the empty triangle's values
# are computed from the bottom up. We can call this type of problem to be one in dynamic programming
if __name__ == "__main__":
	print(TriangleCompute())

# After running this code, we find that the maximum sum of this triangle is given by 1074
# I leave it as an exercise to the reader to find which path generates this answer :P