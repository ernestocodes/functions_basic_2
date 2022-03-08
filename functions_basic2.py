def countdown(num):
    new_list = []
    for x in range(num, -1, -1):
        new_list.append(x)
    return new_list

print(countdown(5))

def print_and_return (list):
    print(list[0])
    b = list[1]
    return b

print(print_and_return([1,2]))

def first_plus_length(list):
    sum =list[0] + len(list)
    return sum

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
    if len(list) <2:
        return False
    new_list = []
    for x in list:
        if x > list[1]:
            new_list.append(x)
    return new_list

print(values_greater_than_second([3]))

def length_and_value(size,value):
    new_list =[]
    for x in range(0, size):
        new_list.append(value)
    return new_list

print (length_and_value(4,7))
print(length_and_value(6,2))

