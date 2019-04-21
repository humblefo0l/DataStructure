
n = 10
def recursivefib(n):
    if n == 0 or n == 1:
        return n

    return recursivefib(n - 1) + recursivefib(n - 2)

for i in range(10):
    print(recursivefib(i), end=" ")
print()
print("*"*8)

n1= 0
n2 = 1

for i in range(n):
    if i == 0:
        print(n1, end=" ")
        continue
    if i == 1:
        print(n2, end=" ")
        continue

    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3


