def a():
    return 5
print(a())

#Guess: 5 Answer: 5

def a():
    return 5
print(a()+a())

#Guess: 10 Answer: 10

def a():
    return 5
    return 10
print(a())

#Guess: 5 Answer: 5

def a():
    return 5
    print(10)
print(a())

#Guess: 5 Answer: 5

def a():
    print(5)
x = a()
print(x)

#Guess: None Answer: None

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

#Guess: None Answer: Error

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#Guess: 25 Answer: 25

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#Guess: 100, 10 Answer: 100, 10

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#Guess: 7, 14, 21 Answer: 7, 14, 21

def a(b,c):
    return b+c
    return 10
print(a(3,5))

#Guess: 8 Answer: 8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#Guess: 500, 500, 300, 500 Answer: 500, 500, 300, 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#Guess: 500, 500, 300, 500 Answer: 500, 500, 300, 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#Guess: 500, 500, 300, 300 Answer: 500, 500, 300, 300

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#Guess: 1, 3, 2 Answer: 1, 3, 2

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#Guess: 1, 3, 5, 10 Answer: 1, 3, 5, 10