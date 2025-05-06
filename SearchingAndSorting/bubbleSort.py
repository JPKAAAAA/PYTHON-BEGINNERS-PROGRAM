import randomArrayGenerator

def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        count=0
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
        if(count==0):
            break

arr=randomArrayGenerator.randomArrayGenerator()
n=len(arr)
print("BUBBLE SORT")
print("Unsorted array is:")
for i in range(n):
    print(arr[i],end=" ")
print()
bubbleSort(arr)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")