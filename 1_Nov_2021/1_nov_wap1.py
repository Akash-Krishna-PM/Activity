#WAP1
#to get a list of cars from the user and print all the items
#starting with 'l' or 'L'
cars=[]
n=int(input("enter number of cars : "))
for i in range(n):
    item=input(f"enter car name {i+1} :")# Lancer, lamborghini, mclaren,audi,Land Rover
    cars.append(item)

print("cars name statring l ot L are \n")
for i in range(len(cars)):
    if(cars[i][0]=='l' or cars[i][0]=='L'):
        print(cars[i],end='\t')



    
