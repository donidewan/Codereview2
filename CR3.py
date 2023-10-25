def even_sum(n):
    # we start with 1 and 1 
    fib = [1, 1]
    
    # we create sum variable to sum all of even numbers
    even_valued_sum  = 0
    
    # we use while to repeat the whole process of iteration
    # if the last fibonacci is lower than N it will keep repeating
    while fib[-1] <= n:
        
        #if the last fibonacci is even number it will be added 
        #to even_valued_sum
        if fib [-1] % 2 == 0:
            even_valued_sum += fib[-1]
        
        #add the last fibonacci addition to the last sequence
        fib.append(fib[-1] + fib[-2])
    
    #call the even_valued_sum variable
    return even_valued_sum