print("Enter the number of elements in array: ",end="")
num=int(input())
array=[]
print("Enter te elements in array")
for x in range(0,num):
  ele=int(input())
  array.append(ele)

for i in range(1,num):
  for j in range(num-i):
    if array[j+1]<array[j]:
      temp=array[j+1]
      array[j+1]=array[j]
      array[j]=temp

print(array,end=" ")

 
