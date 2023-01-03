def gcd(a,b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if ((a % i == 0) and (b % i == 0)):
            usg = i
    return usg
print(gcd(10,5))