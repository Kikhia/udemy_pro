from django.shortcuts import render
from befo_app.models import UserProfileInfo
from django.contrib.auth.models import User
from .forms import UserForm,UserProfileInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'insert' : 'befo kikhia'}
    return render(request,'index.html',context)

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     dic = {'user': user_list}
#     return render(request,'users.html',dic)

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user  = user_form.save()
            user.set_password(user.password)
            user.save()

            profile  = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    dic = {'user_form':user_form,
          'profile_form':profile_form,
          'registered':registered}

    return render(request,'registration.html',dic)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('you are logged in!')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('NOT ACTIVE')
        else:
            print('username: {} password: {}'.format(username,password))
            return HttpResponse('invalid login details')
    else:
        return render(request,'login.html')
