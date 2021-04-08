def binarySearch(arr,first,last,key):
    if(last>=first):
        mid=int(first+(last-first)/2)
        if(arr[mid]==key):
            return mid
        if(key<arr[mid]):
            return binarySearch(arr,first,mid-1,key)
        if(key>arr[mid]):
            return binarySearch(arr,mid+1,last,key)
    else:
        return -1
print("Enter the size of the array:")
n=int(input())
print("Enter the array elements seperated by space in sorted order:")
arr=list(map(int,input().strip().split()))[:n]
print("Enter the element to find:")
key=int(input())
first=0
last=n-1
result=binarySearch(arr,first,last,key)
print(result)