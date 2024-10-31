def is_prime (n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True
    
while True:
    
    try:
        nr1 = int(input('Please choose a number: '))
    except ValueError:
        print('Please enter a valid number')
        continue
    except 

    if (is_prime(nr1) == True):
        print("😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛😛")
    else:
        print("The Numner is NOT prime :(")

            
