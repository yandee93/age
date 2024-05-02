driving = input('你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit # 表示讓程式停在這邊
age = input('你今年幾歲?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('讚喔，你很守法。')
	else:
		print('未成年駕駛，讚喔目中無法。')
elif driving == '沒有':
    if age >= 18:
    	print('快去考駕照吧!')
    else:
    	print('再等幾年吧!')