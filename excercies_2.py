d = {5:{6:3}, "hi":{18:12},"no":{100:"go"}, 50:{2:20}}
def dict_append(data):
    
    sum = 0
    for value in data.values():
        try:
            for value2 in value.values():
                sum += value2
                print(sum)
        except:
            pass
    data["max"] = sum
    return data
print(dict_append(d))

