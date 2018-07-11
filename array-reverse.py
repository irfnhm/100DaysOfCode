arr = [1, 2, 3, 4, 5, 6]

def reverse(arr):
    rev_arr = []
    for i in arr[::-1]:
        rev_arr.append(i)

    for x in rev_arr:
        print(x)

reverse(arr)
