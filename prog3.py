def is_ideal(num:int):
    i = 1 
    sum = 0 
    while i <= num // 2:
        if num % i == 0:
            sum += i
    return true if sum == num else false
        
n = int(input("insert number: "))
print(is_ideal(n))
