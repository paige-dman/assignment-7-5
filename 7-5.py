def isSubset(numbers1, numbers2):
    if len(numbers1) > len(numbers2):
        return False
    
    for i in range(len(numbers2) - len(numbers1) + 1):
        if numbers2[i:i+len(numbers1)] == numbers1:
            return True
        
    return False

print(isSubset([1,2,3], [0,1,2,3,4]))
