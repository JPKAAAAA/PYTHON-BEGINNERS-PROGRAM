import randomArrayGenerator

def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        minIndex=i
        for j in range(i+1,n):
            if(arr[j]<arr[minIndex]):
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]

arr=randomArrayGenerator.randomArrayGenerator()
n=len(arr)
print("SELECTION SORT")
print("Unsorted array is:")
for i in range(n):
    print(arr[i],end=" ")
print()
selectionSort(arr)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")