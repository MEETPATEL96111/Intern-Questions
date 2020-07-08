def printMax(arr, n, k):
    maximum = 0
    for i in range(n - k + 1):
        maximum = arrayy[i]
        for j in range(1, k):
            if arrayy[i + j] > maximum:
                maximum = arrayy[i + j]
        print(str(maximum) + " ", end="")
arrayy = [8,5,10,7,9,4,15,12,90,13]
n = len(arrayy)
k = 4
printMax(arrayy, n, k)

