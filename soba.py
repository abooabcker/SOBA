from prettytable import PrettyTable
t=PrettyTable(['Particulars','Quantity','Rate'])
amount=int(input("\033[30m"+" Enter the amount :\033[1;31m "))
bal=0
n1000=0
n500=0
n100=0
n50=0
n20=0
n10=0
n5=0
n2=0
n1=0
a=amount
rs=set([1000,500,100,50,20,10,5,2,1])
lst=[]
print("\033[m")
print ("\033[30m  Particulars you need \n NB: After complete press 0\033[31m ") 
while True:
    i=input()
    if i==0:
        break
    
    lst.append(i)
lst.sort()
sl=set(lst)
newlist=list(sl)
newlist=sl&rs
cl=list(newlist)
n=len(cl)
cl.sort()
print("\033[30m")
print ("\033[1;47m Y O U   E L E C T")
for i in range(n):
    print(cl[i])
if a >999 and 1000 in newlist:
    n1000=1
    a=a-1000
    
if a >499 and 500 in newlist:
    n500=1
    a=a-500
if a >99 and 100 in newlist :
    n100=1
    a=a-100
if a >49 and 50 in newlist:
    n50=1
    a=a-50
if a >19 and 20 in newlist:
    n20=1
    a=a-20
if a >9 and 10 in newlist:
    n10=1
    a=a-10
if a>4 and 5 in newlist:
    n5=1
    a=a-5
if a>1 and 2 in newlist:
    n2=1
    a=a-2
if a >0 and 1 in newlist :
    n1=1
    a=a-1
if a >0:
    if a>999 and 1000 in newlist:
        b=a//1000
        c=1000*b
        a=a-c
        n1000=n1000+b
    if a>499 and 500 in newlist:
        a=a-500
        n500=n500+1
    if a>99 and 100 in newlist:
        b=a//100
        c=100*b
        a=a-c
        n100=n100+b
    if a >49 and 50 in newlist:
        a=a-50
        n50=n50+1
    if a >19 and 20 in newlist:
        b=a//20
        c=b*20
        a=a-c
        n20=n20+b
    if a>9 and 10 in newlist:
        a=a-10
        n10=n10+1
    if a >4 and 5 in newlist:
        a=a-5
        n5=n5+1
    if a>1 and 2 in newlist:
        b=a//2
        c=b*2
        a=a-c
        n2=n2+b
    if a >0 and 1 in newlist:
        n1=n1+a
        a=a-a
    if a>0:
        bal=a
        

    



if 1000 in newlist:
      t.add_row([1000,n1000,n1000*1000])
if 500 in newlist:
      t.add_row([500,n500,n500*500])
if 100 in newlist:
      t.add_row([100,n100,n100*100])
if 50 in newlist:
      t.add_row([50,n50,n50*50])
if 20 in newlist:
      t.add_row([20,n20,n20*20])
if 10 in newlist:
      t.add_row([10,n10,n10*10])
if 5 in newlist:
      t.add_row([5,n5,n5*5])
if 2 in newlist:
      t.add_row([2,n2,n2*2])
if 1 in newlist:
      t.add_row([1,n1,n1])
    
        

print (t)
print ("BALANCE : {}".format(bal).rjust(30))
print ("TOTAL : {}".format(amount).rjust(30))
