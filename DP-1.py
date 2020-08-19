def solution(N, number):
    dp = [set() for _ in range(9)]
    rep = 0

    for x in range(1, 9):
        rep *= 10
        rep += N
        dp[x].add(rep)
        for i in range(1, x // 2 + 1):
            for num in dp[i]:
                for num2 in dp[x - i]:
                    dp[x].add(num + num2)
                    dp[x].add(num - num2)
                    dp[x].add(num2 - num)
                    dp[x].add(num * num2)
                    if (num2 != 0):
                        dp[x].add(num // num2)
                    if (num != 0):
                        dp[x].add(num2 // num)
        if (number in dp[x]):
            return x;

    return -1