def calc_fib(n,m):
    fibo_list = [0] * (m+1)
    if n>0:
        fibo_list[1] = 1 
        for i in range(2,m+1):
            fibo_list[i] = (fibo_list[i - 1] + fibo_list[i - 2])%10

    return sum(fibo_list[n:m+1])%10

n = input()
a = int(n.split()[0])
b = int(n.split()[1])
print(calc_fib(a,b))