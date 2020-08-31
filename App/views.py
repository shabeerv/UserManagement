from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm  
from .models import Product  

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid username/password!')
            print("Login error")
            return redirect('/')
    else:
        return render(request, 'login.html')

    
def home(request):
    # me = User.objects.all()
    return render(request, 'home.html')


# @login_required
def products(request):
    products = Product.objects.all()  
    products_count = Product.objects.all().count()
    return render(request,"products.html",{'products':products, 'count': products_count})


def addproduct(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/products')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'addproduct.html',{'form':form})  


def time(request):
    return render(request, 'clock.html')



def panel(request):
    userdetails = User.objects.all()
    userscount = User.objects.all().count()
    
    if request.method == "POST":
        username = request.POST['search']
        user = User.objects.get(username=username)
        
        if user is not None:
            return render(request, 'search.html', {'details': user, 'count': userscount})
        else:
            messages.error(request, "User doesn't exist!")
            return render(request, 'search.html')


    return render(request, 'panel.html', {'details': userdetails, 'count': userscount})


def update(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        user.username = username
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.save()
        return redirect('/users/')
    else:
        return render(request,'update.html', {'userinfo': user})


def deluser(request, id):  
    u = User.objects.get(id=id)  
    u.delete()  
    return redirect("/users/")


def adduser(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        print("User Created")
        return redirect('/users/')
    else:
        return render(request, 'adduser.html')


def search(request, username):
    userdetails = User.objects.get(username=username)
    userscount = User.objects.all().count()
    return render(request, 'search.html', {'details': userdetails, 'count': userscount})


def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        print("User Created")

        return redirect('/')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
