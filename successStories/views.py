from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.http import Http404
from PIL import Image
from .models import *
from .forms import *
User=get_user_model()
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def is_owner(func):
    def check_and_call(request, *args, **kwargs):
        # profile=User.objects.get(user=request.user)
        pk = kwargs["id"]
        count=SuccessStories.objects.filter(pk=pk).count()        
        if count>1:
         post=SuccessStories.objects.get(pk=pk)
        
         if not (post.post==request.user): 
            return HttpResponse("<h1>You are not permitted !<h1>", status=404)
        elif count==0:
            return HttpResponse("<h1>You are not permitted !<h1>", status=404)


        return func(request, *args, **kwargs)
    return check_and_call


@login_required(login_url='login')
def SuccessStoriesDisplay(request):
    
    post=SuccessStories.objects.all()

    context={
        'posts':post,
    }
    return render(request,'SuccessStories.html',context)


@login_required(login_url='login')
def SuccessStoriesDisplayDetail(request,id):
    post=SuccessStories.objects.get(pk=id)
    flag=False
    if request.user==post.author:
        flag=True
 
    context={
        'post':post,
        'flag':flag,
    }
    

    return render(request,'SuccessStoriesDetail.html',context,)


@login_required(login_url='login')
def AddSuccessStories(request):
    form=SuccessStoriesForm()
    if request.method=="POST":
        form=SuccessStoriesForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(False)
            obj.author=request.user
            obj.save()
            messages.success(request,"Your data has been saved Successfull")
            return redirect('SuccessStoriesDisplay')
        else:
            messages.success(request,"Data Failed to Save")
            return redirect('AddSuccessStories')
    flag=False
    context={
        'form':form,
        'flag':flag
    }
    return render(request,"SuccessStoriesAdd.html",context)


@is_owner
@login_required(login_url='login')
def UpdateSuccessStories(request,id):
    career=SuccessStories.objects.get(id=id)
    form = SuccessStoriesForm(instance = career)
    if request.method=="POST":        
        form = SuccessStoriesForm(request.POST,instance = career)
        if form.is_valid():  
            form.save()  
            messages.success(request,"Data Updated Successfully")
            return redirect("SuccessStoriesDisplayDetail",id)   
        else:
            messages.success(request,"Data Updation Failed")
            return redirect("SuccessStoriesDisplay")   
    flag=True
    context={'form':form,'flag':flag}
    return render(request,'SuccessStoriesAdd.html',context)


@is_owner
@login_required(login_url='login')
def DeleteSuccessStories(request, id): 
    try:
        career = SuccessStories.objects.get(pk=id)
    except SuccessStories.DoesNotExist:
        return HttpResponse("<h1>Post does not exist</h1>")

    # career = CareerPost.objects.get(id=id)  
    career.delete()  
    messages.success(request,"Data Delete Successfully")

    return redirect("SuccessStoriesDisplay")  