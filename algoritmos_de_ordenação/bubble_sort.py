def main():
    arr1 = [54, 2, 11, 4, 17, 21, 1]
    print("Desordenada ",arr1)
    bubble(arr1)
    print("Ordenada ",arr1)

def bubble(arr):
    sorted = False
    while not sorted:    
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

main()