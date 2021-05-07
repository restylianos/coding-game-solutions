def digit_sum(n:int)->int:
	num_str = str(n) 
	sum = 0
	for i in range(0, len(num_str)):
 		sum += int(num_str[i]) 
	return sum+n #if 11 is the input 11 + 2 = 13 will be the output

r_1 = int(input())
res = 'NO'

for i in range(r_1-1,1,-1):
	r = digit_sum(i)	
	if r == r_1:
		res='YES'
	
print(res)
