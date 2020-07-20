num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
def hcf(a,b):
    if(a<b):
        small=a
    else:
        small=b
    for i in range(1,small+1):
        if((a%i==0)&(b%i==0)):
            h=i
    return h
print("HCF/GCD =",hcf(num1,num2))
        
