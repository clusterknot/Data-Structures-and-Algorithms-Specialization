# Uses python3
import sys
def get_change(m):
    x = [10,5,1]
    total_mon = m
    total_change = 0
    for i in x:
        cnt  = int(total_mon/i)
        total_change = total_change + cnt
        total_mon = total_mon - cnt * i
    return total_change

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
