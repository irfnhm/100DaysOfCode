MyTuple = ("apple", "orange", 100, 10.56, "red", "green")

# prints the items of MyTuple
for t in MyTuple:
    print(t)

# tuple are immutable, this doesn't add the iteme to MyTuple, instead it destroys the old one and creates and new copy of MyTuple
MyTuple = MyTuple.__add__(("yello", "cyan", "teal"))
for t in MyTuple:
    print(t)

#shows the number of items in MyTuple
print(len(MyTuple))

#Tuple items can be accessed using the index values
print(MyTuple[5])
print(MyTuple[8])

