name = "irfan"
machine = "Watson"
caps = name.capitalize()
print("After capitalize:", caps )

flag = name.isalpha()
print(flag)

number = "123"
numFlag = number.isdigit()
print(numFlag)

line = "Some, CSV, values"
newLine = line.split(",")
for value in newLine:
    print(value)

statement = "Nice to meet you {0}. I am {1}".format(name, machine)
print(statement)

a = "  Hello World "
print(a.strip())
print(len(a))

b = "New string"
print(b.upper())

c = "ONE MORE STRING"
print(c.lower())

d = "J am Harry"
print(d.replace("J", "I"))

e = "Python, is, awesome"
print(e.split(","))
