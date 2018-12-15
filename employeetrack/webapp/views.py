from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import signupform, loginform
from webapp.models import employee_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'personal/firstpage.html')

def signup_view(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            username = request.POST.get('username','')
            email = request.POST.get('email', '')
            password = request.POST.get('password','')
            user = User.objects.create_user(username=form.cleaned_data['username'],
			password=form.cleaned_data['password']) #creates user
            spo = employee_info(name = name, username = username, email = email, password = password)
            spo.save() # save data into database

            return HttpResponseRedirect('/login/')
    else:
        form = signupform()

    return render(request, 'personal/signupform.html', {'form': form})

def login_user(request):
	#logout(request)
	form = loginform()
	username = password = ''
	if request.POST:   #form.save()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/webapp/userhome')
		else:
			messages.error(request,"Invalid username or password, please try again.")
	else:
		form = loginform()

	return render(request, 'personal/login.html', {'form': form})

@login_required(login_url='/login/')
def userhome(request):
    data = employee_info.objects.all()
    return render(request, 'personal/userhome.html', {'data': data})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/webapp/login')
