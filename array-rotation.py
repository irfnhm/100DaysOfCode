# the code is incomplete

arr = [1, 2, 3, 4, 5]

def rotateByOne(arr, n):
    temp = arr[0]
        #do something here


def rotate(arr, d, n):
    for i in range(d):
        rotateByOne(arr, len(arr))

def printArray(arr):
    for i in range(len(arr)):
        print(i);



rotate(arr, 2, len(arr))
printArray(arr)