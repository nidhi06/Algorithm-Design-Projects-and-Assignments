import time
def fibonacci(num): 
    if num == 0:
        return 0
    elif num == 1: 
        return 1
    else: 
        return fibonacci(num-1)+fibonacci(num-2)
def time_taken():
    my_num=int(input("Enter the number: "))
    start=time.time()
    print(fibonacci(my_num))
    end=time.time()
    print(end-start)

        
"""
The The largest number that the recursive algorithm (Algorithm 1.6)
can accept as its argument and compute the answer within 60 seconds: 39 (55.26 seconds),
40th element takes 91.60  seconds
----------------------------------------------------------------------
 The time the iterative algorithm (Algorithm 1.7) 
 takes to compute this answer(39th element): 1.120 seconds
 
"""