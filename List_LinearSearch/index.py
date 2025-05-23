def linear_search(arr, target):
    # Return the index of target, or -1 if not found
    for i in range(len(arr)):
        
        if arr[i]==target:
            return i
    return -1

print(linear_search([4, 2, 7, 1], 1))

# Example: linear_search([4, 2, 7, 1], 7) → 2

def linear_ser(arr1, tar):
    for i in arr1:
        if i==tar:
            return arr1.index(i)
    return -1
print(linear_ser([4, 2, 7, 1], 4))
