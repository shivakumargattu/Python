# 3. Find First & Last Occurrence (Unsorted List)

def first_and_last(arr, target):
    # Return [first_index, last_index] (or [-1, -1] if not found)
    first=last=-1
    first=arr.index(target)
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==target:
            last=i
            return 
    return first,last    
    
            
    
result=first_and_last([5, 2, 3, 2, 4], 2) # → [1, 3]
print(result)
