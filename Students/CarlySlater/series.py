def fib(n):
    """return the nth value in the fibonacci series"""
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a


fib (9)

if __name__ == "__main__":
    print fib(9)
    assert fib(9) == 34
    print "All tests passed"