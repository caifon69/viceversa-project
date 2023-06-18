from django.shortcuts import render

def home(requset):
	return render(requset, 'home.html')

def reverse(requset):
	user_text = requset.GET['usertext']
	reversed_text = user_text[::-1]
	return render(requset, 'reverse.html', {'usertext':user_text, 
		'reversedtext':reversed_text})