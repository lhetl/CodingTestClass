def f(w,c,i,j):
    max(dp[i-1][j-w]+c,dp[i][j])
    dp[i-1][j]