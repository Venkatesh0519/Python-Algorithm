import random
data = [1,2,3,4,5,6]
def linear_search(data,result):
    for i in range((len(data))):
        if data[i]==result:
            value = True
            break
        else:
            value = False
    return value
result=random.randrange(1,10)
print(data)
print(result)
print(linear_search(data,result))
