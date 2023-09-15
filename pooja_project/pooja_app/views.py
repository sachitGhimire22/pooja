from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
from django.shortcuts import render

from .models import Person,Collection
# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def shop(request):
    collections = Collection.objects.all()
    context = {
        "details": request.session.get('person'),
        "collections":collections
    }
    print(context)
    return render(request, "shop.html", context)


def blog(request):
    return render(request, "blog.html")


def cart(request):
    return render(request, "cart.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # print(email,password)
        try:
            persons = Person.objects.get(email=email, password=password)
            messages.success(request, "Logged in successfully")
            request.session['person'] = persons.username
            return redirect(shop)
        except Exception as e:
            print(e)
            messages.error(request, "Password or email incorrect")
            return redirect('signup')
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        lastName = request.POST["lastName"]
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            newPerson = Person(first_name=first_name, lastName=lastName,
                               username=username, password=password, email=email)
            newPerson.save()
        except:
            return redirect('signup')

    return render(request, "signup.html")


def home(request):
    return render(request, "index.html")
