def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    first_max_index = 0
    for first in range(1,n):
        if numbers[first] > numbers[first_max_index]:
           first_max_index = first
        
    if first_max_index == 0 :
        second_max_index = 1
    else:
        second_max_index = 0

    for second in range(1,n):
        if (second != first_max_index)  and (numbers[second] > numbers[second_max_index]):
           second_max_index = second 

    return numbers[first_max_index] * numbers[second_max_index]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
