from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm
from .forms import RawProductForm

from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout

from django.views.generic import ListView

# creating pages view here
# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request, 'home.html', {})

def about_view(request,*args,**kwargs):
    return render(request, 'about.html', {})


# creating detials views of products here
def product_detail_view(request,id):
    
    obj = Product.objects.get(id=id)

    # context = {
    #     'title' : obj.title,
    #     'description' : obj.description
    # }
    context = {
        'object' : obj
    }
    return render(request, 'products/detail.html', context)

# letting non-superusers to add data to forms/blogs/sites

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()


#     context = {
#         'form' : form
#     }
#     return render(request, 'products/create.html', context)


# letting non-superusers to add data to forms/blogs/sites creating by raw method
@login_required(login_url='login')
def RawProductForm_view(request):

    form = RawProductForm()

    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)



    context = {
        'form' : form
    }
    return render(request, 'products/create.html', context)



# create login view

def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # checks value for next=/ variable in url to redirect to last visited page (where user clicked login)
            if 'next' in request.POST:     
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')


    return render(request, 'login_register.html')

#logout
def logout_page(request):
    logout(request)
    return redirect('login')



class books_list_view(ListView):
    model = Product

