# N(1≤N≤1,000,000)
# N의 다음 큰 숫자는 N을 2진수로 바꾸었을 때의 1의 개수와 같은 개수로 이루어진 수입니다.
# 1번째 조건을 만족하는 숫자들 중 N보다 큰 수 중에서 가장 작은 숫자를 찾아야 합니다.
######################################
def is_bin_match(bin_n, nxt_bin_n):
    if bin_n에 있는 1의 개수 == nxt_bin_n:
		return True
	return False

def get_next_big_num(n):
	bin_n = bin(n)
	nxt_n = n + 1
	nxt_bin_n = bin(nxt_n)
	
	while is_bin_match(bin_n, nxt_bin_n) :
		nxt_n += 1
		nxt_bin_n = bin(nxt_n)
	
	return nxt_bin_n
	
######################################
def is_bin_match(bin_n, nxt_bin_n):
    if str(bin_n).count('1') == str(nxt_bin_n).count('1') :
        return True
    return False

def nextBigNumber(n):
	bin_n = bin(n)
	nxt_n = n + 1
	nxt_bin_n = bin(nxt_n)
	while is_bin_match(bin_n, nxt_bin_n) is False:
		nxt_n += 1
		nxt_bin_n = bin(nxt_n)
	return nxt_n

print(nextBigNumber(78))