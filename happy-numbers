def sumOfDigits(number:int)->int:
    sum = 0
    while (number!=0):
        dig = number % 10
        sum += dig * dig
        number = number // 10
    return sum

def isHappyNumber(number:int)->bool:
    foundnums=[]
    foundnums.append(number)
    while (True):
        if (number == 1): return True
        number = sumOfDigits(number)
        if number in foundnums: return False
        foundnums.append(number)
    return False

n = int(input())
for i in range(n):
    x = int(input())
    print(f"{x} :)") if isHappyNumber(x) else print(f"{x} :(")
