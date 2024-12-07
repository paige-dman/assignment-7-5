def getMaxElement(numbers):
    max_element = float('-inf')

    for row in numbers:
        for num in row:
            if num > max_element:
                max_element = num


    return max_element

def getSumRows(numbers):
    row_sums = []

    for row in numbers:
        row_sums.append(sum(row))

    return row_sums


numbers = [[99,11,66,8 6,55], [44,21,65,88,24,56], [33,77,32,33,34]]

max_element = getMaxElement(numbers)
print(f"Max Element: {max_element}")

row_sums = getSumRows(numbers)
print(f"Sum of each row: {row_sums}")
