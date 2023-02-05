from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import myUser,Fooditem,Reviews
from .forms import createFooditem,createReviews,Usercreate,NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def homefun(request):
    myhome=Reviews.objects.all()
    return render(request,'homereview.html',{'home':myhome})

def foodfunc(request):
    myfooddet=Fooditem.objects.all()
    return render(request,'fooddetails.html',{'fooddetail':myfooddet})

def userfunc(request):
    myuser=myUser.objects.all()
    return render(request,'userdetails.html',{'myuser':myuser})

def upload_review(request):
    myreview=createReviews()
    if request.method=='POST':
        myreview=createReviews(request.POST,request.FILES)
        if myreview.is_valid():
            myreview.save()
            return redirect('index')
        else:
            return HttpResponse('Your form is worng')
    else:
        return render(request,'review.html',{'review':myreview})

def upload_Food(request):
    myfood=createFooditem()
    if request.method=='POST':
        myfood=createFooditem(request.POST,request.FILES)
        if myfood.is_valid():
            myfood.save()
            return redirect('index')
        else:
            return HttpResponse('your food item is wrong')
    else:
        return render(request,'food.html',{'food':myfood})

def upload_User(request):
    myuser=Usercreate()
    if request.method == 'POST':
        myuser=Usercreate(request.POST,request.FILES)
        if myuser.is_valid():
            myuser.save()
            return redirect('index')
        else:
            return HttpResponse('Your user creation is worng')
    else:
        return render(request,'user.html',{'user':myuser})

def update_review(request,rev_id):
    rev_id=int(rev_id)
    uprev=Reviews.objects.get(id=rev_id)
    rev_form=createReviews(request.POST or None,instance=uprev)
    if rev_form.is_valid():
        rev_form.save()
        return redirect('index')
    return render(request,'review.html',{'review':rev_form})

def delete_review(request,rev_id):
    rev_id=int(rev_id)
    rev_sel=Reviews.objects.get(id=rev_id)
    rev_sel.delete()
    return redirect('index')

def update_food(request,food_id):
    food_id=int(food_id)
    upfood=Fooditem.objects.get(id=food_id)
    food_form=createFooditem(request.POST or None,instance=upfood)
    if food_form.is_valid():
        food_form.save()
        return redirect('index')
    return render(request,'food.html',{'food':food_form})

def delete_food(request,food_id):
    food_id=int(food_id)
    food_sel=Fooditem.objects.get(id=food_id)
    food_sel.delete()
    return redirect('index')

def update_user(request,user_id):
    user_id=str(user_id)
    upuser=myUser.objects.get(Username=user_id)
    user_form=Usercreate(request.POST or None,instance=upuser)
    if user_form.is_valid():
        user_form.save()
        return redirect('index')
    return render(request,'user.html',{'user':user_form})

def delete_user(request,uname):
    uname=str(uname)
    user_sel=myUser.objects.get(Username=uname)
    user_sel.delete()
    return redirect('index')

def register_request(request):
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,'Regiseration Successful')
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


