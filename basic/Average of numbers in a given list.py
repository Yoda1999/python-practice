n=int(input("Enter the number of elements to be stored in the list"))
a=[]
def avg_no_in_list(n):
    for i in range(n):
        s=int(input('Enter the element'))
        a.append(s)
    avg=sum(a)/len(a)
    return avg
print('average =', avg_no_in_list(n))
