import math
def print_divisors(num):
    arr = []
    length = math.sqrt(num) +1 #+1 because range() is not inclusive of the final step
    for i in range(1,int(length)):
        if num % i == 0:
            arr.append(i)
            if num//i == i:
                break
            else:
                arr.append(num//i)
    print(sorted(arr))
    print(34.897)
    return arr


print_divisors(36)
