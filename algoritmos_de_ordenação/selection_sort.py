def main():
    arr1 = [54, 2, 11, 4, 17, 21, 1]
    print("Desordenada ",arr1)
    selection(arr1)
    print("Ordenada ",arr1)
def selection(arr):
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]

main()