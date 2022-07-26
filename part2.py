
#########################
# Author: Zouber Ismail
# Exam
# Date july 26 2022
#########################




def kthsmallest(arr,k):
    """
    Sorting list of number in ascending order
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
    """
    Calculates the sum of the digits in a given number
    Args: 
        -int, number 
    Returns: int, sum of the digits
    
    """
    if num == 0:
        return num
    return num%10 + sum_digits(int(num/10))

def volume(dimensions):
    """
    Calculates volume for a list of dimensions 
    Args: 
        -list, dimensions to caculate volume
    Returns: list, x most frequent words
    
    """
    return dimensions[0]*dimensions[1]*dimensions[2]
def sortvolumes(sequence):
    """
    Sort a 2d array by volume
    Args: 
        -list, volume dimensions to be sorted
    Returns: list, sorted list of dimensions by volume
    
    """
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
    """
    Sorts a list of words by most frequent occurrences 
    Args: 
        -str, words 
        -int, top number of the most frequent words 
    Returns: list, x most frequent words
    
    """
    arr_words = word.split()
    unique_list = {}
    frequency_arr = [None for x in range(len(arr_words))]
    for item in arr_words:
        if item not in unique_list:
            unique_list[item] = 1
        else:
            unique_list[item] += 1
            
    for key in unique_list:
        if key not in frequency_arr:
            frequency_arr[unique_list[key]] = [key]
            
        else:
            frequency_arr[unique_list[key]].append(key)
       
    count = 0
    last = len(frequency_arr)-1
    output = []
    while 0 <= count < num and count < len(unique_list):
        if frequency_arr[last] != None:
            for x in range(len(frequency_arr[last])):
                print(frequency_arr[last][x])
                output.append(frequency_arr[last][x])
            count += 1
        last -= 1
            
        
    return output
        
    


def is_valid_series(num_list,number,sum):
    for x in range(len(num_list)):
        temp_sum = num_list[x]
        for j in range(x+1,number):
            temp_sum += num_list[j]
        if temp_sum > sum:
            return False
    return True
      
if __name__ == "__main__":
    
    is_num = xmostfrequent("peach apple peach orange apple peach", 5)
    print(is_num)