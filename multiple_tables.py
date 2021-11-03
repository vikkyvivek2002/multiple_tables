r= int(input("chose the table "))
n= int(input("range of the table"))
x= int(input("starting point of the table"))
for i in range(x,n+1,1):
    print(r,'*',i,'= ',r*i)
