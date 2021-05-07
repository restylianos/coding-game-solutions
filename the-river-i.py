def digit_sum(n:int)->int:
	num_str = str(n) 
	sum = 0
	for i in range(0, len(num_str)):
 		sum += int(num_str[i]) 
	return sum

r_1 = int(input())
r_2 = int(input())

while(1):
	if r_1 < r_2:		
		r_1 += digit_sum(r_1) 
	else:
		if (r_1==r_2): break
		r_2 += digit_sum(r_2)
print(r_1)
