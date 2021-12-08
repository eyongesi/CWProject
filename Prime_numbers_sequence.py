n = 100
seq = [] # Initialising the prime number sequence list.

for i in range(1, n + 1):
    if i>1:
        for j in range(2, int(i)):
            if i%j == 0:
                break
        else:
            seq.append(i)

print(seq)