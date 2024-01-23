def gen_fib():
    fibinput = int(input("How many Fibonacci numbers to generate?  "))
    i = 1
    if fibinput == 0:
        fib = []
    elif fibinput == 1:
        fib = [1]
    elif fibinput == 2:
        fib = [1,1]
    elif fibinput > 2:
        fib = [1,1]
        while i < (fibinput - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
        return fib

print(gen_fib())