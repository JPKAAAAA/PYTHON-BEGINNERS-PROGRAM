import randomArrayGenerator

def merge(arr,start,mid,end):
    n=end-mid
    temp=[]
    for i in range(n):
        a=arr[mid+i+1]
        temp.append(a)
    j=n-1;
    while(j>=0):
        if(mid>=start and arr[mid]>temp[j]):
            arr[end]=arr[mid]
            end-=1
            mid-=1
        else:
            arr[end]=temp[j]
            end-=1
            j-=1
        
def mergeSort(arr,start,end):
    if(start<end):
        mid=start+(end-start)//2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)

arr=randomArrayGenerator.randomArrayGenerator()
n=len(arr)
print("MERGE SORT")
print("Unsorted array is:")
for i in range(n):
    print(arr[i],end=" ")
print()
mergeSort(arr,0,n-1)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")   