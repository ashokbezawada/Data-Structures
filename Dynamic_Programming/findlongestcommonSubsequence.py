# The main goal of this function is to find the longest common subsequence
# The function takes arguments as two strings

def findlongestcommonSubstring(str1,str2):
    m = len(str1)
    n = len(str2)

    # Creating a matrix
    lcs = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    print(lcs[m][n])
    return lcs[m][n]




# main
str1 = "AGGTAB"
str2 = "GXTXAYB"
findlongestcommonSubstring(str1,str2)