driving = input('请问你有没有开过车？')
if driving != '有' and driving != '没有':
	print('只能输入有/没有')
	raise SystemExit
age = input('请问你的年龄？')
age = int(age)
if driving =='有':
	if age >= 18:
		print('你通过测验了？')
	else:
		print('奇怪，你怎么会有开过车')
elif driving == '没有':
    if age >= 18:
    	print('你可以考驾照了')
    else :
    	print('很好，再过几年就可以考啦')
else:
	print('只能输入有/没有')