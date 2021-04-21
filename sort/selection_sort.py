def selection_sort(A: list):
    # 전체를 순차적으로 탐색한다
    for i in range(len(A)):
        # 아직 정렬되지 않은 영역의 최솟값을 찾는다
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        # 찾은 최솟값과 첫번째 요소의 위치를 바꾼다
        A[i], A[min_idx] = A[min_idx], A[i]

A = [3, 7, 2, 1, 8, 5, 9, 0, 6, 4]
selection_sort(A)
print(A)
