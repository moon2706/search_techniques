def fibonacci_search(arr, x, n):
    n=len(arr)
    search = x
    fibm2 = 0
    fibm1 = 1
    fibm = fibm1 + fibm2

    while(fibm < n):
        fibm2 = fibm1
        print("fibm2 = ",fibm2)
        fibm1 = fibm
        print("fibm1 = ",fibm1)
        fibm = fibm1 + fibm2
        print("fibm = ",fibm)
        print("fibm < n = ",fibm < n)
        print("----")

    offset = -1

    while(fibm > 1):
        i = min(offset + fibm2, n-1)
        print("i = ",i)
        print("@@@@")

        if (arr[i] < x):
            fibm = fibm1
            print("fibm = ",fibm)
            fibm1 = fibm2
            print("fibm1 = ",fibm1)
            fibm2 = fibm - fibm1
            print("fibm2= ",fibm2)
            offset = i
            print("i = ",i)
            print("arr[i] < x = ",arr[i] < x)
            print("........")

        elif (arr[i] > x):
            fibm = fibm2
            print("fibm = ",fibm)
            fibm1 = fibm1 - fibm2
            print("fibm1 = ",fibm1)
            fibm2 = fibm - fibm1
            print("fibm2 = ",fibm2)

        else:
            return i
            print("i = ",i)

    if (fibm1 and arr[n-1] == x):
        return n-1
        print("n-1 = ",n-1)

    return -1

arr = [10,22,35,40,45,50,80,82,85,90,100,235]
n = len(arr)
print("arr = ", arr)
x = int(input("Enter the search element: "))
ind = fibonacci_search(arr,x,n)
if ind >= 0:
    print("Found at index: ", ind)
else:
    print(x," isn't present in the array")