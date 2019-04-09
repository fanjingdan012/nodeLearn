try:
    import psyco

    psyco.full()
except ImportError:
    pass


def count_changes(amount_cents, coins):
    n = len(coins)
    # max([]) instead of max() for Psyco
    cycle = max([c + 1 for c in coins if c <= amount_cents]) * n
    print('cycle',cycle)
    table = [0] * cycle
    for i in range(n):
        table[i] = 1
    for x in range(0, cycle):
        print(x,':',table[x])
    pos = n
    for s in range(1, amount_cents + 1):
        print('s',s)
        for i in range(n):
            print('i',i)
            if i == 0 and pos >= cycle:
                pos = 0
            if coins[i] <= s:
                q = pos - coins[i] * n
                print('q',q)
                table[pos] = table[q] if (q >= 0) else table[q + cycle]
                print(pos,'=',table[pos])
            if i:
                table[pos] += table[pos - 1]
                print(pos, '=ifi', table[pos])
            pos += 1
    return table[pos - 1]


def main():
    us_coins = [ 25, 10, 5, 1]
    eu_coins = [200, 100, 50, 20, 10, 5, 2, 1]

    # for coins in (us_coins, eu_coins):
    print(count_changes(100, us_coins))
        # print
        # count_changes(100000, coins)
        # print
        # count_changes(1000000, coins)
        # print
        # count_changes(10000000, coins), "\n"


main()