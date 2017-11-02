#곱하는 수: 9999이하 >> n이 2이상이니까 1, 2를 곱하고 나열해서 9자리를 넘지 않아야 한다.
#(9999*2=5자리)

#팬디지털 판별!
def is_팬디지털(알고싶은_수):
   팬디지털_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
   num_list = list(알고싶은_수)#list(re.sub('\D', '', 곱셈식))
   if num_list에 팬디지털_list가 다 있으면:
      return True
   else:
      return False

      
def cal_formula(어디부터, 어디까지):
   for num in range(어디부터, 어디까지):
      result_list = []
      for n in range(1, 6):   #곱할 수 있는 가장 작은 수인 2를 해보면 6을 곱할 때 8자리다. 인간적으로 1은 빼자.
         result_list.append(str(num*n))
         ...
         ...