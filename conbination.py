def combination(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        k = arr[i]
        rest = arr[i + 1:]
        for c in combination(rest, n - 1):
            result.append([k] + c)

    return result


arr = [1, 2, 3, 4, 5]
n = 3
print(combination(arr, n))