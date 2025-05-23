# 2. Count Occurrences of a Number


def count_occurrences(arr, target):
    # Return how many times target appears
    count=0
    i=0
    len_arr=len(arr)
    while  i<len_arr:
        if arr[i]==target:
            count+=1
        i+=1
    return count
result=count_occurrences([1, 2, 2, 2, 3,0,0,0,0 ], 1)
print(result)
        
# Example: count_occurrences([1, 2, 2, 2, 3], 2) → 3

def count_occurrence(arr, target):
    count=0
    for i in arr:
        if i==target:
            count+=1
    return count

result1=count_occurrence([2,3,4,44,4,4,4,4,4],4)
print(result1)        
