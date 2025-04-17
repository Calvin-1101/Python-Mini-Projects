import math
def check_prime(num):
    #remember what is a prime number
    #it is a number that only has 2 factors: 1 and itself
    count = 0
    length = math.sqrt(num) +1
    for i in range(1,int(length)):
        if num % i == 0:
            count += 1

            if num//i != i:
                count += 1 

    if count > 2:
        print("It is not a prime number")
    else:
        print("It is a prime number")
        

check_prime(23)


        
