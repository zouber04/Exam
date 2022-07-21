def nextprime(number):
    
    is_prime = False
    next_prime = number+1
    
    for x in range(2,next_prime):
        if next_prime%x == 0:
            next_prime += 1
            
        else:
            return next_prime
        
if __name__ == "__main__":
    nextprime(number):
        print(nextprime)
    