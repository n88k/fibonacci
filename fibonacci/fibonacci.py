def fib(n):
    if n in {0,1}:
        return n
    else:
        return fib(n-2)+fib(n-1)
    
