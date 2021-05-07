l = []
n = int(input())
mul_nums = []
step_3_list = []

for i in range(n):
    card = input()
    rev_car = card[::-1]
    res = rev_car.split()
   
    for token in res:
        for i in range(len(token)):
            if i == 1 or i==3:
                mul_nums.append(int(token[i]) * 2)
    for i in range(len(mul_nums)):
        if mul_nums[i] >= 10:
            mul_nums[i] -= 9
            
    for token in res:
        for i in range(len(token)):
            if i ==0 or i == 2:
                step_3_list.append(token[i])

    
    step_2_res = sum(map(int, mul_nums))
    step_3_res = sum(map(int, step_3_list))

    res = step_2_res + step_3_res
    print('YES') if res%10 == 0 else print('NO')
   
    step_3_list.clear()
    mul_nums.clear()
