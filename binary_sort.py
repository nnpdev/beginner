def binary(arr,x):
    low = 0
    high = len(arr)-1
    while low <=high:
        mid = (low+high)//2
        if arr[mid] > x:
            high = mid -1
        elif arr[mid] < x:
            low = mid + 1
        else:
            return mid
        
arr = [1,2,3,4,5]
x = 4
print(binary(arr,x))        

