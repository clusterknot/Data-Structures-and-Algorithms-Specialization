# Uses python3
import sys

def get_change(m):
    #write your code here
    if m==0:
        return 0
    table = [0 for i in range(m + 1)]
    table[0] = 0
    for i in range(1, m + 1):
        table[i] = sys.maxsize
    coins = [1,3,4]
    for i in range(1, m + 1):
        for j in range(len(coins)):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m  = int(input())
    print(get_change(m))