# Write a program to find the number of ways in which we can transform a wrong word to a correct word by removing zero or more characters from the wrong word. Given: strings, i.e. S1 (for wrong word) and S2 (for correct word).


# Example 1:
# Input :
# Indiiian - String S1, i.e. wrong word 
# Indian - String S2, i.e. correct word


# Output:
# 3 


# Explanation: The three ways will be "ind..ian", "indi.an" and "ind.i.an" is where a character is removed.


# Example 2:
# Input :
# ggoog - String S1, i.e. wrong word 
# go - String S2, i.e. correct word

# Output:
# 4

# Explanation: 
# The four ways will be "g.o..", "g..o.",
# ".go.." and ".g.o.," "." is where characters are removed.



def helper(string1, string2):
	n = len(string1)
	m = len(string2)
	distinct_num = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

	for j in range(n + 1):
		distinct_num[0][j] = 1

	for i in range(m + 1):
		for j in range(n + 1):
			if string1[j - 1] != string2[i - 1]:
				distinct_num[i][j] = distinct_num[i][j - 1]
			else:
				distinct_num[i][j] = distinct_num[i][j - 1] + distinct_num[i - 1][j - 1]

	print(distinct_num)
	return distinct_num[m-1][n-1]

def countTransformation(a, b):
    n = len(a)
    m = len(b)
    if n == m:
        return 0
    if m == 0:
        return 1
    dp = [[0] * (n) for _ in range(m)]
    for i in range(m):
        for j in range(i, n):
            if i == 0:
                if j == 0:
                    if a[j] == b[i]:
                         dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif a[j] == b[i]:
                    dp[i][j] = dp[i][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
            else:
                if a[j] == b[i]:
                     dp[i][j] = (dp[i][j-1] + dp[i-1][j-1])
                else:
                    dp[i][j] = dp[i][j-1]
    return dp[m-1][n-1]

if __name__ == "__main__":
    a = input()
    b = input()
    print(countTransformation(a,b))


string1, string2 = input(), input()
result = helper(string1, string2)
print(result)