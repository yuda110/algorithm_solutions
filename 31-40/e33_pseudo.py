#>>분자(numerator), 분모(denominator)의 숫자를 일단 ['9', '8']과 같이 리스트로 뽑은 후에 비교해서 같은 수 고르기?
#>>아니면 같은 수를 넣고나서 분자 분모를 만들기?


#11, 22 등과 같은 경우는 예외 처리
exception_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

def make_분자_분모_리스트():
	분자분모_list = []
	for 분자 in range(11, 99):
		for 분모 in range(10, 98):
			#반드시 분자 > 분모
			if 분자 <= 분모 or 분자 in exception_list or 분모 in exception_list:
				break
			else :
				분자_list = list(str(분자))	#['3', '4']
				분모_list = list(str(분모))	#['5', '3']
				#분자와 분모에 같은 수가 '하나만' 존재
				for num in 분자_list:
					if num in 분모_list:
						overlap_num = num
				분자분모_list.append([분자, 분모, overlap_num])
				
	return 분자분모_list