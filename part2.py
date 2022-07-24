




def intersection(arr_one,arr_two):
    pass

def kthsmallest(arr,k):
    """
    Sorting list of number in asceding order
    Args: 
        -int array, numbers
    Returns: int array, sorted numbers

    """
    
    size = len(arr)
    output = [0] * size

    # count array initialization
    count = [0] * (size+3)

    # storing the count of each element 
    for m in range(0, size):
        count[arr[m]] += 1

    # storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]
        
    return arr[k+1]


def sum_digits(num):
    if num == 0:
        return num
    return num%10 + sum_digits(int(num/10))

def volume(dimensions):
    return dimensions[0]*dimensions[1]*dimensions[2]
def sortvolumes(sequence):
    length = len(sequence)
    
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    items_lower = []
    items_greater = []
    
    for item in sequence:
        if volume(item) > volume(pivot):
            items_greater.append(item)
            
        else:
            items_lower.append(item) 
            
    return sortvolumes(items_lower) + [pivot] + sortvolumes(items_greater)

def xmostfrequent(word, num):
    arr_words = word.split()
    unique_list = []
    for item in arr_words:
        if item not in unique_list:
            unique_list.append(item)
    
    sorted_arr = quicksort(unique_list, arr_words)
    output = []
    if num > len(sorted_arr):
        return sorted_arr
    else:
        for x in range(num):
            output.append(sorted_arr[x])
            
        return output    
def frequency(word, arr_words):
    count = 0
    
    for x in arr_words:
        if word in arr_words:
            count += 1
    return count
       
def quicksort(unique, arr_words):
    """
    Sort array of points based off euclidean distance from ascending order
    Args: 
        -array, unsorted points
    Returns: array, Sorted points

    """
    length = len(unique)
    
    if length <= 1:
        return unique
    else:
        pivot = unique.pop()

    items_greater = []
    items_lower = []
    

    for i in range(len(unique)):
        if frequency(unique[i],arr_words) > frequency(pivot,arr_words):
            items_greater.append(unique[i])

        else:
            items_lower.append(unique[i])
        

    return quicksort(items_lower,arr_words) + [pivot] + quicksort(items_greater,arr_words)      
      
if __name__ == "__main__":
    num = xmostfrequent("peach apple peach orange apple peach", 4)
    print(num)