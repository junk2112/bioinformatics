
import sys

def min_coins(coins, value):

    result = [0] + [sys.maxint for i in range(0, value)]
    for i in range(1, value + 1):
        for coin in coins:
            if coin <= i:
                sub_result = result[i - coin]
                if sub_result + 1 < result[i]:
                    result[i] = sub_result + 1
    return result[-1]

value = 19283
coins = sorted([int(item) for item in "1,3,5".strip().split(",")], reverse=False)
print(min_coins(coins, value))
