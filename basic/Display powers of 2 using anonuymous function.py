n=int(input('Enter the number:'))
terms = list(map(lambda x: 2 ** x, range(n+1)))
for i in range(n+1):
    print("2 raised to the power ",i,"is",terms[i])
