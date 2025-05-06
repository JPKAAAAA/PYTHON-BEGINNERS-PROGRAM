import randomArrayGenerator

def radixSort(arr):
    n=len(arr)
    max1=max(arr)
    exp=1
    while(max1//exp>0):
        count=[0]*10
        output=[0]*n
        for i in range(n):
            count[(arr[i]//exp)%10]+=1
        for i in range(1,10):
            count[i]+=count[i-1]
        i=n-1
        while(i>=0):
            output[count[(arr[i]//exp)%10]-1]=arr[i]
            count[(arr[i]//exp)%10]-=1
            i-=1
        for i in range(n):
            arr[i]=output[i]
        exp*=10

arr=randomArrayGenerator.randomArrayGenerator() 
n=len(arr)
print("RADIX SORT")
print("Unsorted array is:")
for i in range(n):
    print(arr[i],end=" ")
print()
radixSort(arr)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")