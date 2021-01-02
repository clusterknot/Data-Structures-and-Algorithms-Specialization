def gcd(a,b) :
    if a >= b:
        smaller = b
        larger = a
    else:
        smaller = a
        larger  = b
    rem = larger%smaller
    if  rem ==0:
        return smaller
    while rem !=0:
        rem = larger % smaller
        if rem == 0:
            return smaller
        larger = smaller
        smaller = rem

n = input()
a = int(n.split()[0])
b = int(n.split()[1])
print(gcd(a,b))
