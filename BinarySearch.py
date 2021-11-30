array = [1,2,3,4,5]
def BiarySearch(array,target):
    start, end= 0 , len(array)-1
    while start <= end:
        mid = int((start + end) / 2)
        if(target == array[mid]):
            return mid
        elif(target < array[mid]):
            end = mid - 1 
        else:
            start = mid + 1
    return None
print(BiarySearch(array, 7))