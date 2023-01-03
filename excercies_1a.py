def gdc(a,b):
    if a > b:
        small = b
    else:
        small = a
    i = 1
    while i <= small:
        if a % i == 0 and b % i == 0:
            usg = i
        i +=1 
    return usg
print(gdc(10,5))