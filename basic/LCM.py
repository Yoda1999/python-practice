num1=int(input('Enter the first number'))
num2=int(input('Enter the second number'))
def lcm(a,b):
    if a>b:
        great=a
    else:
        great=b
    while(True):
        if((great%a==0)&(great%b==0)):
            l=great
            break
        great+=1
    return l
print('LCM =',lcm(num1,num2))
