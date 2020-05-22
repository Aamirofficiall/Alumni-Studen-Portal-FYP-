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
        count=TechTrend.objects.filter(pk=pk).count()        
        if count>1:
         post=TechTrend.objects.get(pk=pk)
        
         if not (post.post==request.user): 
            return HttpResponse("<h1>You are not permitted !<h1>", status=404)
        elif count==0:
            return HttpResponse("<h1>You are not permitted !<h1>", status=404)


        return func(request, *args, **kwargs)
    return check_and_call


@login_required(login_url='login')
def TechTrendDisplay(request):
    
    post=TechTrend.objects.all()

    context={
        'posts':post,
    }
    return render(request,'TechTrend.html',context)


@login_required(login_url='login')
def TechTrendDisplayDetail(request,id):
    post=TechTrend.objects.get(pk=id)
    flag=False
    if request.user==post.author:
        flag=True
 
    context={
        'post':post,
        'flag':flag,
    }
    

    return render(request,'TechTrendDetail.html',context,)


@login_required(login_url='login')
def AddTechTrend(request):
    form=TechTrendForm()
    if request.method=="POST":
        form=TechTrendForm(request.POST)
        if form.is_valid():
            obj=form.save(False)
            obj.author=request.user
            obj.save()
            messages.success(request,"Your data has been saved Successfull")
            return redirect('TechTrendDisplay')
        else:
            messages.success(request,"Data Failed to Save")
            return redirect('AddTechTrend')
    flag=False
    context={
        'form':form,
        'flag':flag
    }
    return render(request,"TechTrendAdd.html",context)


@is_owner
@login_required(login_url='login')
def UpdateTechTrend(request,id):
    career=TechTrend.objects.get(id=id)
    form = TechTrendForm(instance = career)
    if request.method=="POST":        
        form = TechTrendForm(request.POST,instance = career)
        if form.is_valid():  
            form.save()  
            messages.success(request,"Data Updated Successfully")
            return redirect("TechTrendDisplayDetail",id)   
        else:
            messages.success(request,"Data Updation Failed")
            return redirect("TechTrendDisplay")   
    flag=True
    context={'form':form,'flag':flag}
    return render(request,'TechTrendAdd.html',context)


@is_owner
@login_required(login_url='login')
def DeleteTechTrend(request, id): 
    try:
        tech = TechTrend.objects.get(pk=id)
    except TechTrend.DoesNotExist:
        return HttpResponse("<h1>Post does not exist</h1>")

    # career = CareerPost.objects.get(id=id)  
    tech.delete()  
    messages.success(request,"Data Delete Successfully")

    return redirect("TechTrendDisplay")  