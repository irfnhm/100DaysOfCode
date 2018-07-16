box = [10, 3, 45, 76, 565, 65, 12, 43,78]

def findMinimum(box):
    min = box[0]
    for i in range(len(box)):
        if min > box[i]:
            min = box[i]

    print("Minumum is: ", min)


def findMaximum(box):
    max = box[0]
    for i in range(len(box)):
        if max < box[i]:
            max = box[i]

    print("Maximum is: ", max)


findMinimum(box)
findMaximum(box)
