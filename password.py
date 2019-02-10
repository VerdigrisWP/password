#檢查密碼
pw = 'a123456'
i = 3
while i > 0:
	input_pw = input('請輸入密碼：')
	i = i - 1
	if input_pw == pw:
		print('密碼正確')
		break
	else:
		if i > 0:
			print('密碼錯誤，請重新輸入', '你還有', i, '次機會')
		else:
			print('密碼錯誤，請下次再來')
