def calc_fib(n):
    fibo_list = [0] * (n+1)
    
    if n>0:
        fibo_list[1] = 1 
        
        for i in range(2,n+1):
            fibo_list[i] = (fibo_list[i - 1] + fibo_list[i - 2])%10
            

        
    return sum(fibo_list) % 10

n = int(input())
print(calc_fib(n))