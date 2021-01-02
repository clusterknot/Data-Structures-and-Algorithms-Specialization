#python3
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

def lcm(a,b):
    gr = gcd(a,b)
    if gr == 1:
        return int(a*b)
    gr2 = 1
    while gr != 1:
        gr = gcd(a,b)
        gr2 = gr2 * gr
        a = a/gr
        b = b/gr
        if gr == 1:
            return int(gr2*a*b)
n = input()
a = int(n.split()[0])
b = int(n.split()[1])
print(lcm(a,b))


