num = input("Kindly Enter a Positive number: ")
if not num.isdigit():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

elif num.isdigit():
    order = len(num)
    sum = 0
    for i in num:
        sum += pow(int(i),order)
    if sum == int(num):
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong Number.")   
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")