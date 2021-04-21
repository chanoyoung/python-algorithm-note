def insertion_sort(A: list):
    # Traverse through 1 to len(A)
    # Consider 0 is already sorted
    for i in range(1, len(A)):
        key = A[i]

        # Move elements that are greater than key
        # to one position behind
        j = i-1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        # Insert key to the right position
        A[j + 1] = key

A = [3, 7, 2, 1, 8, 5, 9, 0, 6, 4]
insertion_sort(A)
print(A)
