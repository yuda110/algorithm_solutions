#p <= 1000 직각삼각형
#a^2 + b^2 = c^2

#1) p의 값을 기준으로, {a, b, c} 값을 정한다.

def get_삼각형의_세변(p):
	직각삼각형_cnt = 0
	for a in range(어디부터, p-2까지):
		for b in range(어디부터, p-2까지):
		c = p - (a + b)
		if 	a^2 + b^2 == c^2 :
			직각삼각형_cnt += 1
	return 직각삼각형_cnt
	
def get_max....