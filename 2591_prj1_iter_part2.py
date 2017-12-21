
import time                     # import the time package to use system time
def fibonacci(num):              # iter_fib --> iterative fibonacci
                                 # num --> user enters the number to generate fibonacci sequence
                                  
 start = time.time()            # we calculate the time ,that the function starts executing
 
 num0,num1 = 0,1                # the element at 0th position is 0, assign it to num0
                                 # the element at 1st position is 1,assign it to num1  
                                
 for i in range(0, num): 
     num0,num1=num1,num0 + num1   
                                  
                                     # we calculate the time ,that the function stops executing
 print(time.time()-start)            # calculate the total time taken for the function to execute
 

 print ("Output:", num0)            # return the num-th number in the fibonacci series
                                    
    
                       
"""
The The largest number that the recursive algorithm (Algorithm 1.6)
can accept as its argument and compute the answer within 60 seconds: 39 (55.26 seconds),
40th element takes 91.60  seconds
----------------------------------------------------------------------
 The time the iterative algorithm (Algorithm 1.7) 
 takes to compute this answer(39th element): 1.120 seconds
 
"""                    
                                
     
        
        
     
             
           
    
    
                     
                        
              
                          

