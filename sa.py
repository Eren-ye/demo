data = [1,2,3,4,5]
sub = list(map(lambda n : n - 1,data))
print(sub)

data = [1,2,3,4,5]
def add(n):
    return n + 1
add = list(map(add, data))
print(add)

users = ['Ram','sita','hari','sophia','gp']
def length_greater():
    for user in users:
        if len(user) > 4:
            print(user)

length_greater()

def add(x,y):
    print(x + y)
add(5,3)

#lambda
add = lambda x, y: x + y
print(add(5, 3))  

def sub(x,y):
    print(x - y)
sub(5,3)

sub = lambda x,y : x - y
print(sub(5,3))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)