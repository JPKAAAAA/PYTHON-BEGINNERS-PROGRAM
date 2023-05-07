#this program prints triangle of numbers using nested for loop

print("Enter number of rows:",end="")
rows=int(input())
for i in range(rows):   
    for j in range(i+1):
        print(j+1,end="")
    print("")