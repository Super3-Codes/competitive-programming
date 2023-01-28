def insertionSort1(n, arr):
    # Write your code here
    aux = []
    j = 0
    for i in range(n):
        aux = arr[i]
        j = i - 1
        while j >= 0 and aux < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            print(*arr)
        arr[j+1] = aux
    print(*arr)
