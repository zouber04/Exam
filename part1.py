#########################
# Author: Zouber Ismail
# Exam part 1
# Date july 11 2022
#########################
def nextprime(number):
    """
    Finding the next prime number
    Args: 
        -int, a number
    Returns: int, the next prime number

    """
    
    is_prime = False
    next_prime = number
    while is_prime == False:
        next_prime += 1
        prime = 0
        for x in range(2,next_prime):
            if next_prime%x == 0:
                prime = 1
                
        if prime == 0:
            is_prime = True        
          
        
    return next_prime        
def calculate_area(dimension):
    """
    Calculate the area of a triangle given a list of dimensions
    Args: 
        -list, dimensions
    Returns: int, area of a triangle

    """
    area = 0.5*dimension[0]*dimension[1]
    return area
def minarea(arr):
    """
    Sorts a list of dimensions from a 2d array
    Args: 
        -list, dimensions
    Returns: int, the next prime number

    """
    
    lowest = arr[0]
    
    for x in range(1,len(arr)):
        temp_low = calculate_area(arr[x])
        if temp_low < calculate_area(lowest):
            lowest = arr[x]
    return lowest  

def count(arr,num):
    """
    Counts number of occurrences in an array
    Args: 
        -list, array of numbers
        -int, number to scan for
    Returns: int, number of occurrences

    """
    count = 0
    for x in range(len(arr)):
        if arr[x] == num:
            count += 1
    return count
def mode(arr):
    """
    Returns the mode in an array
    Args: 
        -list, numbers
    Returns: int, the mode

    """
    highest = arr[0]
     
    for x in range(1,len(arr)):
        temp_high = count(arr,arr[x])
        if temp_high > count(arr,highest):
            highest = temp_high
            
    return highest
             
if __name__ == "__main__":
    mode_list = [8, 3, 2, 8, 1, 7, 2, 0, 4, 2, 5]
    print(mode(mode_list))
    