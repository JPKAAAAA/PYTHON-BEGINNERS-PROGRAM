import randomArrayGenerator

def countSort(arr):
    """n=len(arr)
    maxElement=max(arr)
    count=[0]*(maxElement+1)
    for i in range(n):
        count[arr[i]]+=1
    i=0
    for j in range(maxElement+1):
        while(count[j]>0):
            arr[i]=j
            i+=1
            count[j]-=1"""
    
    n=len(arr)
    maxEle=arr[0]
    for i in range(1,n):
        if(arr[i]>maxEle):
            maxEle=arr[i]
    temp=[]
    for i in range(maxEle+1):
        temp.append(0)
    for i in range(n):
        temp[arr[i]]+=1
    for i in range(1,maxEle+1):
        temp[i]+=temp[i-1]
    output=[]
    for i in range(n):
        output.append(0)
    for i in range(n-1,-1,-1):
        output[temp[arr[i]]-1]=arr[i]
        temp[arr[i]]-=1
    for i in range(n):
        arr[i]=output[i]

arr=randomArrayGenerator.randomArrayGenerator()
n=len(arr)
print("COUNT SORT")
print("Unsorted array is:")
for i in range(n):
    print(arr[i],end=" ")
print()
countSort(arr)
print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")