# 動的計画法(DP)
s=input()
words = {"dream", "dreamer", "erase", "eraser"}

dp = dict()
dp[0] = 1
for i in range(0, len(s)):
    if not dp.get(i):
        continue
    for word in words:
        if s[i:i+len(word)] == word:
            dp[i+len(word)] = 1

print("YES" if dp.get(len(s)) else "NO")