# Fibonacci sequence: f(0)=0; f(1)=1; f(n)=f(n-1) + f(n-2)

def fib_num(n):
     
    if n <= 0:
        return [0]
    else:
        fi = [0,1] # Initialising the Fibonacci sequence list for 0 and 1.
        for x in range (2, 11):
            fn = fi[-1] + fi[-2] # Fibonacci sequence
            fi.append(fn)
        return fi
fi = fib_num(10)[1:11]
# fib_list = list(range(fib_num()))
print(fi)