def fibonacci(n):
    ele1, ele2 = 0, 1               # the first and second elements are 0 and 1
    for i in range(0, n):
        ele1, ele2 = ele2, ele1 + ele2
    return ele1