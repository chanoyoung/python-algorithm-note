def bubble_sort(A: list):
    n = len(A)

    for i in range(n - 1):
        for j in range(n - i - 1):
            # Swap if the element is greater
            # than the next element
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

A = [3, 7, 2, 1, 8, 5, 9, 0, 6, 4]
bubble_sort(A)
print(A)
