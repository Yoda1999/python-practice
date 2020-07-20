number=int(input('Enter an integer'))
a=[]
for i in range(2,number):
    if(number%i==0):
        a.append(i)
a.sort()
print('The Smallest divisor is',a[0] )
