from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from .forms import UpdateUserForm
from django.template import RequestContext
from .forms import LoginForm
from django.contrib import messages


def LoginView(request):
    logout(request)
    email = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
        else:
            messages.success(request, 'Email or Password is incorrect')
    form=LoginForm()
    return render(request,'login.html',{'form':form})



@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            # profile=Profile.objects.create(user=user)
            # profile.save()
            username=form.cleaned_data.get('email')
            messages.success(request,'Account has been created for u '+str(username))
            return redirect('login')
 
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})


@login_required(login_url='login')
def UpdateUser(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request,"User is update successfully")
            return redirect('update')
    form = UpdateUserForm(instance=request.user)
    args = {'form': form}
    return render(request, 'editUser.html', args)


@login_required(login_url='login')
def UpdatePassword(request):
    if request.method == 'POST':
        user=request.user
    
        form = PasswordChangeForm(data=request.POST, user=user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,"Password update successfully")
            return redirect('password')
        else:
            messages.success(request,"Password worn't mathch")
            return redirect('password') 
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)

