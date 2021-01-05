# Uses python3
import sys



def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort() #nlogn
    count, max_ele, temp, f = 0, -1, a[0], 0

    for i in range(left,right):
        # increases the count if the same element occurs
        # otherwise starts counting new element
        if(temp == a[i]) :
            count += 1
        else :
            count = 1
            temp = a[i]
             
        # sets maximum count
        # and stores maximum occured element so far
        # if maximum count becomes greater than n/2
        # it breaks out setting the flag
        if(max_ele < count) :
            max_ele = count
            ele = a[i]
             
            if(max_ele > (len(a)//2)) :
                f = 1
                break
        
    # returns maximum occured element
    # if there is no such element, returns -1
    if f == 1 :
        return ele
    else :
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    # input  = input()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)