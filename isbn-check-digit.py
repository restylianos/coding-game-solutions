def isISBN(inputISBN:str)->bool:
    if len(inputISBN) == 10 or len(inputISBN) == 13:
        for i in range(len(inputISBN)):
            if not inputISBN[i].isdigit() and i!=len(inputISBN)-1:
                return False
        return True
    return False

def validateISBN10(inputISBN:str)->bool:
    res=0
    for i in range(len(inputISBN)-1):
        res += int(isbn[i]) * (10-i)
    if(inputISBN[9].isdecimal()):
        return False if  (res + int(inputISBN[9])) % 11 != 0 else True
    else:
        return False if (res + 10) % 11  != 0 else True

def validateISBN13(inputISBN:str)->bool:
    res=0
    for i in range(len(inputISBN)-1):
        if(i%2==0):
            res += int(isbn[i]) * 1
        else:
            res += int(isbn[i]) * 3
    if((inputISBN[12]).isdecimal()):
        return False if (res + int(inputISBN[12])) % 10 else True
    else:
        return False

invalid = list()
n = int(input())

for i in range(n):
    isbn = input()
    if not isISBN(isbn):
        invalid.append(isbn)
        continue
    if len(isbn) == 10:
        if not validateISBN10(isbn):
            invalid.append(isbn)
    if len(isbn) == 13:
        if not validateISBN13(isbn):
            invalid.append(isbn)        

print(len(invalid),"invalid:")
for i in invalid:
    print(i)
