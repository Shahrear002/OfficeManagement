from django.shortcuts import render
from django.http import HttpResponse
from .forms import signupform, loginform
from webapp.models import employee_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'personal/firstpage.html')
"""
def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = User.objects.create_user(username=form.cleaned_data['username'],
			password=form.cleaned_data['password']) #creates user
            spo = patient_info(name = name, username = username, password = password, address = address, contactnumber = contactnumber)
            spo.save() # save data into database

            return HttpResponseRedirect('/login/')
    else:
        form = signupform()

    return render(request, 'personal/signupform.html', {'form': form})
"""

def login(request):
	'''logout(request)
	form = loginf()
	username = password = ''
	if request.POST:   #form.save()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/userhome/')
		else:
			messages.error(request,"Invalid username or password, please try again.")
	else:
		form = loginf()'''

	return render(request, 'personal/login.html')
