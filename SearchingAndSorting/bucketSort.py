import randomArrayGenerator

def bucketSort(arr):
    n=len(arr)
    maxVal=max(arr)
    minVal=min(arr)
    rangeVal=maxVal-minVal
    bucketSize=rangeVal//n
    bucket=[]
    for i in range(n):
        bucket.append([])
    for i in range(n):
        index=(arr[i]-minVal)//bucketSize
        if(index==n):
            index-=1
        bucket[index].append(arr[i])        
    for i in range(n):
        bucket[i].sort()
    index=0
    for i in range(n):
        for j in range(len(bucket[i])):
            arr[index]=bucket[i][j]
            index+=1

arr=randomArrayGenerator.randomArrayGenerator()
n=len(arr) 
print("BUCKET SORT")
print("Unsorted array is:")
for i in range(n):
    print(arr[i],end=" ")
print()
bucketSort(arr)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ") 