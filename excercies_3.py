T = ((20,"hi"),(40,"like"),(60,"lock"),(80,"look"))
def function(data):
    my_tuple = ()
    i = 0
    while i < len(data):
        if data[i][1][0] == "l":
            my_tuple += (data[i][0],)
        i+=1
    small = min(my_tuple)
    big = max(my_tuple)
    for number in range(1,small+1):
        if small % number == 0  and big % number == 0:
            usg = number
    return my_tuple,number
print(function(T))