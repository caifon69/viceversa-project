from django.shortcuts import render

def home(requset):
	return render(requset, 'home.html')

def reverse(requset):
	user_text = requset.GET['usertext']
	reversed_text = user_text[::-1]
	number_of_words = len(user_text.split())
	return render(requset, 'reverse.html', {'usertext':user_text, 
		'reversedtext':reversed_text, 'numberofwords':number_of_words})