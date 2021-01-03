# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    value_per_weight = [float(j/i) for i, j in zip(weights,values)]
    weights = [x for y,x in sorted(zip(value_per_weight,weights),reverse=True)]
    value_per_weight = [y for y,x in sorted(zip(value_per_weight,weights),reverse=True)]
    total_cap_re = capacity
    for i,j in zip(value_per_weight,weights):
        if total_cap_re>=j:
            value = value + j*i
            total_cap_re = total_cap_re - j
        elif total_cap_re==0:
            break
        else:
            value = value + total_cap_re*i
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
