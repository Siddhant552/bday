from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def invalid_page(request):
    return render(request, 'invaliddetails.html')

@login_required
def page1(request):
    return render(request, 'page1.html')

@login_required
def page2(request):
    return render(request, 'page2.html')

@login_required
def page3(request):
    return render(request, 'page3.html')

@login_required
def page4(request):
    return render(request, 'page4.html')

@login_required
def page5(request):
    return render(request, 'page5.html')

@login_required
def page6(request):
    return render(request, 'page6.html')

@login_required
def page7(request):
    return render(request, 'page7.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('page1'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username : {} and password: {}".format(username,password))
            return HttpResponseRedirect(reverse("invaliddetails"))

    else:
        return render(request, 'login.html')
