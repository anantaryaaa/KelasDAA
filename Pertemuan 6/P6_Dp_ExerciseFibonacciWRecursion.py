def Rec_Fib(n):
    if n <= 1:
        return n
    else:
        return (Rec_Fib(n-1) + Rec_Fib(n-2))

nterms = int(input("How many terms? "))

# check if nterms value is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(Rec_Fib(i))