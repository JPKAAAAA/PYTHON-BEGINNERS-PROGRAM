def linearSearch(arr,searchElement):
    for i in arr:
        if searchElement in arr:
            return 1
        else:
            return 0

arr=[]
noOfElements=int(input("Enter number of element: "))
for i in range(noOfElements):
    temp=int(input())
    arr.append(temp)
searchElement=int(input("Enter element to be searched: "))
result=linearSearch(arr,searchElement)
if result:
    print("Element found in the array")
else:
    print("Element not found in the array")