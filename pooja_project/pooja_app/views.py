from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Item,Cart
# Create your views here.
from django.shortcuts import render

from .models import Person, Collection
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
        "collections": collections
    }
    print(context)
    return render(request, "shop.html", context)


def product_details(request, id):
    collection_response = Collection.objects.get(id=id)
    item_response = Item.objects.filter(category_id=id)
    context = {
        "collection_detail": collection_response,
        "items": item_response,
        "details": request.session.get('person-id'),
    }

    return render(request, "sproduct.html", context)

def view_cart(request):
    matchedCart = Cart.objects.filter(person_id = request.session.get('person-id'))
    item_list = []
    for item in matchedCart:
        matched_item = Item.objects.filter(item_name=item.item_id).get()
        item_list.append(matched_item)
    #try
    print(item_list)
        
    context = {
        "cartdetails":matchedCart,
        "itemdetails":item_list
    }
    return render(request,'cart.html',context)


def blog(request):
    return render(request, "blog.html")


def add_to_cart(request,product_id,item_id,item_quantity,price):
    print(item_id)
    try:
        item = Item.objects.get(pk=item_id)
        person = Person.objects.get(pk=request.session.get("person-id"))
        Cart.objects.create(
            item_id=item,
            quantity=item_quantity,  
            price = price,
            person_id =person  # You can adjust this as needed
        )
        messages.success(request,"Added to cart")
    except Exception as e:
        print(e)
        messages.error(request,"Couldnot add to cart")
        print("Adding failed")
    
    
    return redirect ('../../../../../product_details/'+str(product_id))
    
    



def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # print(email,password)
        try:
            persons = Person.objects.get(email=email, password=password)
            messages.success(request, "Logged in successfully")
            request.session['person'] = persons.username
            request.session['person-id'] = persons.id
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
