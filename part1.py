def nextprime(number):
    
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
    area = 0.5*dimension[0]*dimension[1]
    return area
def minarea(arr):
    
    lowest = arr[0]
    
    for x in range(1,len(arr)):
        temp_low = calculate_area(arr[x])
        if temp_low < calculate_area(lowest):
            lowest = arr[x]
    return lowest  

def count(arr,num):
    count = 0
    for x in range(len(arr)):
        if arr[x] == num:
            count += 1
    return count
def mode(arr):
    highest = arr[0]
     
    for x in range(1,len(arr)):
        temp_high = count(arr,arr[x])
        if temp_high > count(arr,highest):
            highest = temp_high
            
    return highest
             
if __name__ == "__main__":
    mode_list = [8, 3, 2, 8, 1, 7, 2, 0, 4, 2, 5]
    print(mode(mode_list))
    