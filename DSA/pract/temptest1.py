import sys
 
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
    
if __name__=="__main__":
    import sys
    print(sys.argv[1])
    fib(int(sys.argv[1]))