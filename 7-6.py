def mergeList(num1, num2):
    i, j = 0, 0
    merged = []

    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i += 1

        else:
            merged.append(num2[j])
            j += 1

    while i < len(num1):
        merged.append(num1[i])
        i += 1

    while j < len(num2):
        merged.append(num2[j])
        j += 1

    return merged


num1 = [1,3,5,7]
num2 = [2,4,6,8]
result = mergeList(num1,num2)
print(result)
