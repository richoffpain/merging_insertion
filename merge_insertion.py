"""
Merging one array : 
_ when size is big we divide 
_ when size is small enough , lets say less or equal to 4 we sorted it using the insertion method
_ then we merge all the element when size greater than that
"""
def mergesort(array, low, high, size=4):
    if low < high:
        if (high - low) <= size:
            return insertion(array, low, high)
        else:
            middle = int((low+high) / 2)
            mergesort(array, low, middle)
            mergesort(array, middle + 1, high)
            return merge(array, low, middle, high)

def merge(array, low, middle, high):
    #divide the array into 2 sub arrays

    left = array[low: middle+1]
    right = array[middle+1: high+1]
    k = low
    i = 0
    j = 0
    # comparing the two sorted subarray until one of them becomes empty and adding the smallest element for each comparison on the new array    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k +=1
    # When the bucle is completed that means one array is empty so we have to copy the following element of whateever array that still has element in the new array

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array
def insertion(array, low, high):
    for i in range(len(array) - 1):
        key = array[i + 1]
        #j = i
        while i >= 0 and array[i] > key:
            array[i + 1], array[i] = array[i], array[i+1]
            i -= 1
        
    return array

def main():
    array = [9, 3, 7, 5, 6, 4, 8, 2, 11, 3, 0, 1, 10]
    sorted_array = mergesort(array, 0, len(array) - 1)
    print(sorted_array)

if __name__ == '__main__':
    main()