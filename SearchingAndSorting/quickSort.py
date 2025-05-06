import randomArrayGenerator

def partition(arr,start,end):
    count=0
    for i in range(start,end+1):
        if(arr[i]<arr[start]):
            count+=1
    arr[start],arr[start+count]=arr[start+count],arr[start]
    pivot=start+count
    while(start<pivot and end>pivot):
        if(arr[start]<arr[pivot]):
            start+=1
        elif(arr[end]>=arr[pivot]):
            end-=1
        else:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    return pivot

def quickSort(arr,start,end):
    if(start<end):
        pivot=partition(arr,start,end)
        quickSort(arr,start,pivot-1)
        quickSort(arr,pivot+1,end)

arr=randomArrayGenerator.randomArrayGenerator()
n=len(arr)
print("QUICK SORT")
print("Unsorted array is:")
for i in range(n):
    print(arr[i],end=" ")
print()
quickSort(arr,0,n-1)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")