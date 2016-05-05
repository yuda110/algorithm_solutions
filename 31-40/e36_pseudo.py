#2진수 구하는 함수 있으면 좋은데

def get_2진수(10진수):
	return 2진수
	
def is_대칭수(num):
	if num is 대칭수:
		return  True
	else:
		return False
	
def get_대칭수(range_to):
	result_sum = 0
	for i in range(range_to):
		10진수 = i
		2진수 = get_2진수(10진수)
		if is_대칭수(10진수)==True and is_대칭수(2진수)==True :
			result_sum += 10진수