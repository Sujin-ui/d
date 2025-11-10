def remove_value(lt, number):
    result = []
    for i in lt:
        if i != number:
            result.append(i)
    return result


numbers = [1,2,3,4,5]
result = remove_value(numbers, 2 )
print(result)