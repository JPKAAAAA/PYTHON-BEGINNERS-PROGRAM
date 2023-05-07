print("Enter the number of elements in array: ",end="")
num=int(input())
array=[0]
print("Enter te elements in array")
for x in range(num):
  element=int(input())
  array.append(element)

for i in range(num+1):
  for j in range(num-i):
    if array[j+1]<array[j]:
      temp=array[j+1]
      array[j+1]=array[j]
      array[j]=temp

print(array,end=" ")

 