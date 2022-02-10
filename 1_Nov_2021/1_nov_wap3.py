n=int(input("enter how many numbers - "))
num=[]
for i in range(n):
    item=int(input(f"num{1} : "))
    num.append(item)

for i in range(n):
    if(num[i]>50 and num[i]%2==0):
        print(num[i],end='\t')
