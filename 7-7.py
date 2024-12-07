def hasARE(words):
    result = []

    for word in words:
        a_indexing = word.find('a')
        if a_indexing != -1:
            r_indexing = word.find('r', a_indexing + 1)
            if r_indexing != -1:
                e_indexing = word.find('e', r_indexing + 1)
                if e_indexing != -1:
                    result.append(word)

    return result

words = ['are', 'arrow', 'amore', 'aspire', 'assertive', 'arrogant', 'bartender', 'carter']
result = hasARE(words)
print(result)
