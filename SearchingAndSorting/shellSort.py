import randomArrayGenerator

def shellSort(arr):
    n=len(arr)
    gap=n//2
    while(gap>0):
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap//=2

arr=randomArrayGenerator.randomArrayGenerator()
n=len(arr)
print("SHELL SORT")
print("Unsorted array is:") 
for i in range(n):
    print(arr[i],end=" ")
print()
shellSort(arr)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")
