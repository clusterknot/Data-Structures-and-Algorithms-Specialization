def calc_fib(n):
    fibo_list = [0] * (n+1)
    if n>0:
        fibo_list[1] = 1 

        for i in range(2,n+1):
            fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]
        
    return fibo_list[n]

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        if (previous == 0 and current == 1):
            return i + 1

def fibonacci_h(n,m):
    period = pisanoPeriod(m)
    rem = n % period
    return calc_fib(rem)%m 
n = input()
a = int(n.split()[0])
b = int(n.split()[1])
print(fibonacci_h(a,b))


