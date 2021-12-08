
num = range(1, 101)
for x in num:
    
    if x % 3 == 0 and x % 5 == 0: #  For numbers that are multiples of both 3 and 5, print "FizzBuzz"
        print("FizzBuzz") 
    elif x % 3 == 0: #  if a number is multiple of 3, print "Fizz" instead of this number
        print("Fizz")
    elif x % 5 == 0: #  if a number is multiple of 5, print "Buzz" instead of this number
        print("Buzz")
    
    else:
        print(x)