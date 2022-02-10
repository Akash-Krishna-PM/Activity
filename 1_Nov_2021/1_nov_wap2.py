animals=[]
n=int(input("enter number:"))
for i in range(n):
    item=input(f"animal {i+1}: ")
    animals.append(item)

print("animals whose name is less than or equal to 4 are - ")
for i in range(len(animals)):
    if(len(animals[i])<=4):
        print(animals[i])
