w, h = [int(i) for i in input().split()]
last_bin  =[]
letters = []
final_word = []


for i in range(h):
    for j in input().split():
        pixel = format(int(j),'08b')
        last_bin.append(pixel[len(pixel)-1])

def converter(last_bin:list)->str:
    c=0 #used as counter
    for i in last_bin:
        c+=1
        letters.append(i)
        if c%8==0:
            final_word.append((chr(int("".join(letters),2))))
            letters.clear()
    return f"".join(final_word)

print(converter(last_bin))
