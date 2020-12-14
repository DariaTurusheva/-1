def make_change(coin_value_set, change, coins_used):
    min_coins = [0] * (change + 1)
    for i in range(change + 1):
        coin_count = i
        new_coin = 1
        for j in [c for c in coin_value_set if c <= i]:
            if min_coins[i - j] + 1 < coin_count:
                coin_count = min_coins[i - j] + 1
                new_coin = j
        min_coins[i] = coin_count
        coins_used[i] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


coins = {int(x) for x in input().split()}
amount = int(input())

used_coins = [0] * (amount + 1)

print(make_change(coins, amount, used_coins), "монеты:")

print_coins(used_coins, amount)
