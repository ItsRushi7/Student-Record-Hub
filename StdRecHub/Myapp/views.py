from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from Myapp.models import Records

# Create your views here.

def Login(request):

    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user = authenticate(username=user_name, password=pass_word)

        if user != None:
            login(request,user)
            messages.success(request, "Login Successfully ")
            return redirect('Home')
        
        else:
            messages.error(request, "Invalid username and password")
            return redirect('Login')
    
    return render(request, 'index.html')


def signup(request):

    
    if request.method == 'POST':
        username = request.POST.get('Name')
        mobile = request.POST.get('Number')
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        if (username != '' and mobile != '' and email != '' and password != ''):

            Sign_up = User.objects.create_user(
                username=username, email=email, password=password)
            Sign_up.save()
            messages.success(request, "Signup Successfuly")
            return redirect('Login')

    return render(request, 'Signup.html')


def Home(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')

        obj = Records()

        obj.name = name
        obj.surname = surname
        obj.dob = dob
        obj.email = email
        obj.phone = phone
        obj.address = address

        obj.save()

    data = Records.objects.all()

    return render(request, 'Home.html', {'data': data})

def Delete(request, id):

    obj = Records.objects.get(id=id)
    obj.delete()

    return redirect('Home')

def Edit(request, id):

    data = Records.objects.get(id=id)

    if request.method == 'POST':

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')

        obj = Records.objects.get(id=id)

        obj.name = name
        obj.surname = surname
        obj.dob = dob
        obj.email = email
        obj.phone = phone
        obj.address = address

        obj.save()

        return redirect('Home')

    return render(request, 'Edit.html',{'data': data})


# def Update(request,id):

    



