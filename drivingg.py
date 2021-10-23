country = input('請問你是哪國人： ')
age = input("請問你幾歲： ")
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('之後才能考')
