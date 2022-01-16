n = int(input("Enter number of terms"))

n1 = 0
n2 = 1
i = 0

if n <= 0:
    print("Enter positive integer")
elif n == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while i < n:
        print(n1)
        n3 = n1 + n2
    
        n1 = n2
        n2 = n3
        i += 1
