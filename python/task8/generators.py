"""count fibonachi sequence"""
import types


# fill in this function
def fib():
    """this generator count fibonachi sequence
    """
    fib1 = 1
    fib2 = 1

    for _ in range(8):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2


# testing code

if isinstance(fib(), types.GeneratorType):
    print("Good, The fib function is a generator.")

    COUNTER = 0
    for n in fib():
        print(n)
        COUNTER += 1
        if COUNTER == 10:
            break
