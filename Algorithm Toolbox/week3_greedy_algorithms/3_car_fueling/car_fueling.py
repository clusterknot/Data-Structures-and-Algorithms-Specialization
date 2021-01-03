# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refill = 0
    n = len(stops)
    if stops[0]>tank:
        return -1
    stops.append(distance)
    stops.append(0)
    stops.sort(reverse=False)
    fuel_left = tank
    for i in range(1,n+1):
        dist_travel = stops[i]
        fuel_left =  fuel_left - (stops[i] - stops[i-1])
        if (fuel_left < 0):
            return -1
        if stops[i+1] - stops[i] > fuel_left:
            num_refill = num_refill + 1
            fuel_left = tank
        if i==n:
            dist_left  = distance - dist_travel
            if fuel_left < dist_left:
                return -1
    return num_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))


