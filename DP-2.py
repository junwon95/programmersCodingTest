def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    dp[0].append(triangle[0][0])

    for i in range(1, len(triangle)):
        for j in range(0, i + 1):
            if (j == 0):
                dp[i].append(dp[i - 1][j] + triangle[i][j])
            elif (j == i):
                dp[i].append(dp[i - 1][j - 1] + triangle[i][j])
            else:
                dp[i].append(triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j]))

    return max(dp[len(triangle) - 1])

# calculate the largest path sum from the top, unsing previous dp[] as reference