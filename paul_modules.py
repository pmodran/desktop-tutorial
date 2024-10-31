def multiply(x,y):
    return x * y

def add(x,y):
    return x + y

def substract(x,y):
    return x-y

def devide(x,y):
    return x/y

def is_prime(x):
    if x<=1:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if (x%i == 0):
                return False
        return True
    
def is_even(x):
    if (x%2 == 0):
        return True
    return False

def maximum(x):
    max = x[0]
    for i in x:
        if (i>max):
            max = i
    return(max)    

