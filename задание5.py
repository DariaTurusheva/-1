# longest common subsequence of 3 = lcs
def lcs(x, y, z):
    l = [[[0 for _ in range(len(z)+1)] for j in range(len(y)+1)] for k in range(len(x)+1)]

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            for k in range(1, len(z) + 1):
                if (i == 0) and (j == 0) and (k == 0):
                    l[i][j][k] = 0
                elif (x[i-1] == y[j-1]) and (y[j-1] == z[k-1]):
                    l[i][j][k] = l[i-1][j-1][k-1] + 1
                else:
                    l[i][j][k] = max(max(l[i-1][j][k], l[i][j][k-1]), l[i][j-1][k])
    return l[len(x)][len(y)][len(z)]


if __name__ == '__main__':
    print(lcs('abcd1e2',
              'bc12ea',
              'bd1ea')
          )