from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.core.mail import send_mail
# Create your views here.

def index(request):
	if request.method=="POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		subject = request.POST.get("subject")
		message = request.POST.get("message")
		try:
			message = "Message from " + name + " with email " + email + "\n" + message
			to = ['rjrjjoshirahul@gmail.com', 'puranjay.makhija@gmail.com', 'puranjay25m@gmail.com']
			send_mail(subject, message, 'rjrjjoshirahul@gmail.com',to,fail_silently=False)
			return redirect("main:index")
		except Exception as e:
			raise e
			return redirect("main:index")
	return render(request, "index.html")