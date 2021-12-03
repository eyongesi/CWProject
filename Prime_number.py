num = input("Kindly Enter a Positive natural number: ")

if not num.isdigit():
    print("Kindly Enter a Positive natural number: ")

elif int(num) > 1: 
    for i in range(2, int(num)):
        if (int(num) % int(i)) == 0:
            print("{} is not a prime number".format(num))
            break
    else:
        print("{} is a prime number".format(num))
else:
    print("Kindly Enter a Positive natural number: ") 