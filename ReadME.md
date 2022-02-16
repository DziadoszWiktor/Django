# **Django**
# **1.** Python Virtual Enviornment, basic cmds
Istalling... 

    pip install virtualenv

Creating...

    python -m venv *venv name*

Activating...

    source *venv name*/Scripts/activate

Checking... (*should appear our current directory*)

    pip -V

Installing dependencies from a requirements.txt file

    pip install -r *filename*.txt

Checking dependencies...

    pip freeze

Comment multiple lines in VSCode

    CTRL+K+C

Uncomment multiple lines in VSCode

    CTRL+K+U

# **2.** Creating a new Django project
Creating a new project...

    django-admin startproject *name of the project* .

First running...

    python manage.py runserver

Sync settings and all in db...

    python manage.py migrate

Creating admin user for /admin section ... (wik,wik)

    python manage.py createsuperuser

Creating new app... (app means parts of project, in case of fe. a shop we should have products app, cart app, login app...)

    python manage.py startapp *app name* (products)

Migrations after the creation of new app and after modification of models.py (?)

    python manage.py makemigrations
    python manage.py migrate

Open django shell...

    python manage.py shell

See the all models objects (in the dj shell)

    >>> Product.objects.all()

Create new model object (in the dj shell)

    >>> Product.objects.create(title='...',description="...",...)

# **3.** Project tree

* ### .venv
* ### src
    * #### project
        * ### pycache_
        * ### init_.py
        * ### asgi.py
        * ### settings.py
        * ### urls.py
        * ### wsgi.py
    * #### templates
        * ### files .html
    * #### db.sqlite3
    * #### manage.py
* ###  ReadME.md
(project tree after startapp command)
* ### .venv
* ### src
    * #### app
        * ### pycache_
        * ### migrations (new)
            * ### init_.py
        * ### init_.py (new)
        * ### admin.py (new)
        * ### apps.py (new)
        * ### models.py (new)
        * ### test.py (new)
        * ### views.py (new)
    * #### project
        * ### pycache_
        * ### init_.py
        * ### asgi.py
        * ### settings.py
        * ### urls.py
        * ### wsgi.py
    * #### templates
        * ### files .html
    * #### db.sqlite3
    * #### manage.py
* ###  ReadME.md

# **4.** Settings.py
(comments in trydjango/settings.py)

# **5.** Models.py (app/models.py)
* After the creation of the model we should go to settings.py and add our new app (products in this case) in the INSTALLED_APPS
* https://docs.djangoproject.com/it/4.0/ref/models/fields/ (model field types)
* If I want to add new a field in the model, we have two solutions for the previous objects:
    * set the value field of the old objects to null 

            ...TextField(null=True) or
            ...TextField(default=...)
    * wen the shell offers us the options, if we choose the 1) we can add same values to all old fields
* field requirement blank=False->Required blank=True->Not required

# **6.** Admin.py (app/admin.py)
We can see our model fields in the admin section so in the admin.py we can write:

    from .models import *model class* Product (relative import)
    admin.site.register(Product)

# **7.** views.py
Place to handle the various web pages

Option with single lines of html code
    from django.http import HttpResponse

    def home_view(*args,**kwagrs):
        return HttpResponse("<h1>Hello World</h1>")
Option with html files (we create a temaplates folder/index.html) but we have to add the templates directory into settings.py

    def home_view(*args,**kwagrs):
        return render("templates/index.html", {})

in setting.py in TEMPLATES

    'DIRS': ['/c/Users/VG Rig/Desktop/Uniwersytet/Programowanie/Python/Django (2022)/src/templates'],


# **8.** urls.py (project/urls.py)

    from pages.views import home_view,contact_view (add this)

    urlpatterns = [
        path('', home_view, name='home'), (add this)(views,*name of function view*)
        path('contact/', contact_view, name='contact'), (trying another view)
        path('admin/', admin.site.urls),    
    ]

# **9.** Template enginge intherance

    {% block content%} html code {% endblock *content if not in base* %}

# **10.** Template context
We talked about views

    def home_view(*args,**kwagrs):
        return render("templates/index.html", {})

We left the dict empty, we can write the context in the dict like that

    def home_view(*args,**kwagrs):
        my_context = {
            "my_text"="some text"
            "my_list"=["a","b","c"]
        }
        return render("templates/index.html", my_context)

I can use my dict elments in the templates

    <h1>{{ my_text }}</h1>

We can use a loop too...

    {% for list_item in my_list %}
        <p>{{ forloop.counter }} {{ list_item }}</p>
        <p>{{ forloop.counter }} {{ list_item }}</p>
        <p>{{ forloop.counter }} {{ list_item }}</p>
    {% endfor %}

Or we can use conditions...

    {% if a == a %}
    ...
    {% elif b == b %}
    ...
    {% else %}
    ...
    {% endif %}

We can find others tempate tags in the doc

# **11.** Using views with data models
We can use that in a shop f.e.

    def product_view(*args,**kwagrs):
        obj = Product.objects.get(id=1)
        my_context = {
            "title"="title product"
            "price"=...
            ...
        }
        return render("templates/index.html", my_context)

# **12.** Django Model Forms
We make a forms.py file in the app (products)

    from django import forms
    from .models import Product

    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = [
                "title",
                "description",
                "price",
                "summary",
            ]
We have to add the form in the views.py

    from urllib import request
    from django.shortcuts import render
    from .forms import ProductForm
    from .models import Product


    def product_create_view(reqeust):
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductForm()
        context = {
            "form":form
        }
        return render(request, "./products/product_create.html", context)

we make our html page </br>

    {% extends "./base.html" %}

    {% block content %}
    <div>
        <form method="POST"> {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Save">

        </form>
    </div>
    {% endblock %}

and we add to views.py

    urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('create/', product_create_view), #this
    path('product/', product_detail_view),
    path('admin/', admin.site.urls),
    ]

after all modification if we changed models.py we shoudl run (just in case)

    python manage.py makemigrations
    python manage.py migrate

# **13.** Django Pure Forms
in forms.py

    #the difference between this and Product form is the forms.Form attribute
    #that means this is a standard django form
    class RawProductForm(forms.Form):
        # in the forms module we don't have textfiled only charfield (modified by models.py)
        title = forms.CharField()
        description = forms.CharField()
        price = MoneyField(
            decimal_places=2,
            default=0,
            default_currency='PLN',
            max_digits=10,
        )
        summary = forms.CharField()

in views.py

    def product_create_view(request):
    form = RawProductForm()
    if request == "POST":
        form = RawProductForm(request.POST or None)
    context = {
        "form" : form
    }
    return render(request, "./products/product_create.html", context)

# **15.** Validations
in ProductForm in forms.py

    def validator(self,*args, **kwagrs):
        title = self.cleaned_data("title")
        if not "ok" in title:
            raise forms.ValidationError("nope")

# **16.** Dynamic URL routing

# **17.** .....
# **18.** .....
# **19.** .....
# **20.** .....
# **21.** .....
# **22.** .....
# **23.** .....


<br />
(min 2:45:00 https://youtu.be/F5mRW0jo-U4)

