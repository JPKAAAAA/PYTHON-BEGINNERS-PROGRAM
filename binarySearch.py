import random

def binarySearch(arr,searchElement):
    start=0
    end=len(arr)-1
    count=0
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==searchElement:
            return 1
        elif arr[mid]>searchElement:
            end=mid-1
        elif arr[mid]<searchElement:
            start=mid+1
    return 0
            
def sortingFunction(arr):
    length=len(arr)
    for i in range(length-1):
        for j in range(length-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

no=int(input("Enter no. of elements: "))
arr=[]
print("how will you add elements")
choice=int(input("1)Automatic           2)Manual"))
if(choice==1):
    for _ in range(no):
        arr.append(random.randint(0,99))
    print("Automatic generated Array: ",arr)
elif(choice==2):
    for i in range(no):
        temp=int(input())
        arr.append(temp)
else:
    print("wrong choice")
    exit()
searchElement=int(input("Enter element to be searched: "))
sortingFunction(arr)
print("Sorted Array: ",arr)
result=binarySearch(arr,searchElement)
if(result):
    print("Element found")
else:
    print("Element not found")
