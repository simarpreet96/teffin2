import json
import math
import random
from json import JSONEncoder

from django.contrib.sites import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
# from twilio.rest.api.v2010.account import key
from .messages_send import sendotp
from .models import User, Role, Product, Productgalleryimage, Maincategory, Supercategory, Subcategory, \
    Attribute, Configure, Blog, Blogcategory, Country, City, Variants, Images, Color, Size
from .forms import SignUpForm, AttributeForm, ConfiguresForm, SubcategoryForm, SupercategoryForm, \
    MaincategoryForm, ProductForm, VendorForm, CustomerForm, EmployeeForm, BlogForm, BlogcategoryForm, UserForm, \
    UserLoginForm, SimpleSignUpForm, SimpleLoginForm, CurrentlocationForm
from django.contrib.auth import login, authenticate
from geopy.geocoders import Nominatim
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages, auth
from django.urls import reverse
from django.urls import resolve
from django.contrib.auth.hashers import check_password

key = 'V/eW+6qrm60-Bw8qAXFEKBlvbeOwyrVmMQD5AGl2f5'

from django.contrib.auth.decorators import login_required


# from django.contrib.gis.geoip2 import GeoIP2


# def tiffin_location(request):
#     # g = GeoIP2()
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
#     print(ip)
# def my_view(request):
#     context['location'] = request.location


# def search(request):
#     query = request.GET['query']
#     if len(query) > 50:
#         allpost = Product.objects.none()
#     else:
#         allpost = Product.objects.filter(Q(name__icontains=query) |
#                                          Q(category__icontains=query) |
#                                          Q(detail_text__icontains=query) |
#                                          Q(attribute__icontains=query))
#     if allpost.count() == 0:
#         messages.error(request, 'can not found')
#     return render(request, 'index.html', {'allpost': allpost, 'query': query})


def loginhere(request):
    if request.method == "POST":
        vaddress = request.POST['address']
        request.session['address'] = vaddress   #set session value
        address = request.session.get('address')#get session value
        return redirect('simplesignup')
    return render(request, 'login.html', locals())


# def loginhere(request):
#     if request.method == "POST":
#         vaddress = request.POST['location']
#         geolocator = Nominatim(user_agent="tiffenapp")
#         servicelocation = geolocator.geocode(vaddress, timeout=10000)
#         print(servicelocation.address)
#         request.session['location'] = servicelocation.address   #set session value
#         location = request.session.get('location')      #get session value
#         form = CurrentlocationForm(request.POST)
#         if form.is_valid():
#             ven = form.save(commit=False)
#             ven.currentlocation = servicelocation.address
#             # ven.save()
#             return redirect('simplesignup')
#     else:
#         form = CurrentlocationForm()
#         print(form)
#     return render(request, 'login.html', locals())


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard/index.html')


def vendor_coupon(request):
    return render(request, 'dashboard/coupon-vendor.html')


def user_current_admin(request):
    currentadmin = User.objects.filter(username=request.user)
    return render(request, 'dashboard/admin.html', {'currentadmin': currentadmin})


def current_user_edit(request, slug):
    post = get_object_or_404(User, slug=slug)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('user_current_admin')
    else:
        form = UserForm(instance=post)
    return redirect('user_current_admin', {'form': form})
    # return render(request, 'dashboard/admin.html', {'form': form})


def user_admin_list(request):
    admin_list = User.objects.filter()
    return render(request, 'dashboard/admin.html', {'admin_list': admin_list})


def user_employee_list(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.role.role_id = 2
            emp.save()
            return redirect('user_employee_list')
    else:
        form = EmployeeForm()
    employee_list = User.objects.filter(role__role_id=2)
    return render(request, 'dashboard/employee.html', locals())


def user_employee_del(request, slug):
    post = get_object_or_404(User, slug=slug)
    post.delete()
    return redirect('user_employee_list')


def user_employee_detail(request, slug):
    post = get_object_or_404(User, slug=slug)
    return render(request, 'dashboard/view-employee.html', {'post': post})


def user_employee_edit(request, slug):
    post = get_object_or_404(User, slug=slug)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('user_employee_list')
    else:
        form = EmployeeForm(instance=post)
    return render(request, 'dashboard/employee-edit.html', {'form': form})


def user_customer_list(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            cus = form.save(commit=False)
            cus.role.role_id = 4
            cus.save()
            return redirect('user_customer_list')
    else:
        form = CustomerForm()
    customer_list = User.objects.filter(role__role_id=4)
    return render(request, 'dashboard/customer.html', locals())


def user_customer_del(request, slug):
    post = get_object_or_404(User, slug=slug)
    post.delete()
    return redirect('user_customer_list')


def user_customer_detail(request, slug):
    post = get_object_or_404(User, slug=slug)
    return render(request, 'dashboard/customer-view.html', {'post': post})


def user_customer_edit(request, slug):
    post = get_object_or_404(User, slug=slug)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            # return HttpResponseRedirect('dashboard/user/customer/user-customer-list/')
            abab = '/dashboard/user/customer/user-customer-list/'
            return redirect(abab)
            # return redirect('user_customer_list')
    else:
        form = CustomerForm(instance=post)
    return redirect('user_customer_list', {'form': form})
    # return render(request, 'dashboard/customer-edit.html', {'form': form})


def vendor_detail_index(request, slug):
    post = get_object_or_404(User, slug=slug)
    vendor_pro = Product.objects.filter(user__role__role='vendor') & Product.objects.filter(user__slug=slug)
    return render(request, 'menu.html', locals())


def user_current_location_index(request):
    if request.method == "POST":
        vaddress = request.POST['location']
        geolocator = Nominatim(user_agent="tiffenapp")
        servicelocation = geolocator.geocode(vaddress, timeout=10000)
        print(servicelocation.address)
        request.session['location'] = servicelocation.address   #set session value
        location = request.session.get('location')      #get session value
        form = CurrentlocationForm(request.POST)
        if form.is_valid():
            ven = form.save(commit=False)
            ven.currentlocation = servicelocation.address
            # ven.save()
            return redirect('simplesignup')
    else:
        form = CurrentlocationForm()
        print(form)
    return render(request, 'index.html', locals())


# def user_current_location_index(request):
#     if request.method == "POST":
#         vaddress = request.POST['location']
#         geolocator = Nominatim(user_agent="tiffenapp")
#         location = geolocator.geocode(vaddress, timeout=10000)
#         print(location.address)
#         form = CurrentlocationForm(request.POST)
#         print(form)
#         if form.is_valid():
#             ven = form.save(commit=False)
#             ven.currentlocation = location.address
#             ven.save()
#             print(ven)
#             return redirect('user_vendor_list')
#     else:
#         form = CurrentlocationForm()
#         print(form)
#     return render(request, 'index.html', locals())


def user_vendor_list(request):
    if request.method == "POST":
        vaddress = request.POST['vendor_location']
        # vlongitude = request.POST['vendor_longitude']
        # vlatitude = request.POST['vendor_latitude']
        geolocator = Nominatim(user_agent="tiffenapp")
        location = geolocator.geocode(vaddress, timeout=10000)
        # vlonglocation = geolocator.geocode(vlongitude, timeout=10000)
        # vlatlocation = geolocator.geocode(vlatitude, timeout=10000)
        print(location.address)
        # print(vlonglocation.longitude, vlatlocation.latitude)
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            ven = form.save(commit=False)
            ven.vendor_location = location.address
            # ven.vendor_longitude = vlonglocation.longitude
            # ven.vendor_latitude = vlatlocation.latitude
            ven.role.role_id = 3
            ven.save()
            return redirect('user_vendor_list')
    else:
        form = VendorForm()
    vendor_list = User.objects.filter(role__role_id=3)
    return render(request, 'dashboard/vendor.html', locals())


def user_vendor_edit(request, slug):
    post = get_object_or_404(User, slug=slug)
    if request.method == "POST":
        form = VendorForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect('/dashboard/user/vendor/user-vendor-list')
            # return redirect('user_vendor_list')
    else:
        form = VendorForm(instance=post)
    return redirect('user_vendor_list', {'form': form})
    # return render(request, 'dashboard/vendor.html', locals())


def user_vendor_detail(request, slug):
    post = get_object_or_404(User, slug=slug)
    vendor_pro = Product.objects.filter(user__role__role='vendor') & Product.objects.filter(user__slug=slug)
    vendor_veg = Product.objects.filter(user__role__role='vendor') & Product.objects.filter(
        user__slug=slug) & Product.objects.filter(type='veg')
    vendor_nonveg = Product.objects.filter(user__role__role='vendor') & Product.objects.filter(
        user__slug=slug) & Product.objects.filter(type='non-veg')
    return render(request, 'dashboard/vendor-view.html', locals())


def vendor_allproducts(request):
    vendor_pro = Product.objects.filter(user__role__role='vendor')
    return render(request, 'dashboard/all-vendor-list.html', {'vendor_pro': vendor_pro})


def user_vendor_del(request, slug):
    post = get_object_or_404(User, slug=slug)
    post.delete()
    return redirect('user_vendor_list')


def maincategorylist_edit(request, slug):
    post = get_object_or_404(Maincategory, slug=slug)
    if request.method == "POST":
        form = MaincategoryForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('maincategory_list')
    else:
        form = MaincategoryForm(instance=post)
    return redirect('maincategory_list',
                    {'form': form})  # render(request, 'dashboard/main-category-edit.html', {'form': form})


def maincategory_del(request, slug):
    post = get_object_or_404(Maincategory, slug=slug)
    post.delete()
    return redirect('maincategory_list')


def maincategory_detail(request, slug):
    post = get_object_or_404(Maincategory, slug=slug)
    return redirect('maincategory_list')  # render(request, 'dashboard/main-category-detail.html', {'post': post})


def maincategory_list(request):
    if request.method == "POST":
        form = MaincategoryForm(request.POST, request.FILES)
        if form.is_valid():
            maincategory = form.save(commit=False)
            maincategory.user = request.user
            maincategory.save()
            maincategoryurl = '/dashboard/product-categories/maincategory-list/'
            return redirect(maincategoryurl)
    else:
        form = MaincategoryForm()
    allmaincategory = Maincategory.objects.filter()
    return render(request, 'dashboard/main-category.html', locals())


def supercategorylist_edit(request, slug):
    post = get_object_or_404(Supercategory, slug=slug)
    if request.method == "POST":
        form = SupercategoryForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('supercategory_list')
    else:
        form = SupercategoryForm(instance=post)
    return redirect('supercategory_list',
                    {'form': form})  # render(request, 'dashboard/super-category-edit.html', {'form': form})


def supercategory_del(request, slug):
    post = get_object_or_404(Supercategory, slug=slug)
    post.delete()
    return redirect('supercategory_list')


def supercategory_detail(request, slug):
    post = get_object_or_404(Supercategory, slug=slug)
    return redirect('supercategory_list')  # render(request, 'dashboard/super-category-detail.html', {'post': post})


def supercategory_list(request):
    if request.method == "POST":
        form = SupercategoryForm(request.POST, request.FILES)
        if form.is_valid():
            supercategory = form.save(commit=False)
            supercategory.user = request.user
            supercategory.save()
            supercategoryurl = '/dashboard/product-categories/supercategory-list/'
            return redirect(supercategoryurl)
    else:
        form = SupercategoryForm()
    allsupercategory = Supercategory.objects.all()
    return render(request, 'dashboard/super-category.html', locals())


def subcategorylist_edit(request, slug):
    post = get_object_or_404(Subcategory, slug=slug)
    if request.method == "POST":
        form = SubcategoryForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm(instance=post)
    return redirect('subcategory_list',
                    {'form': form})  # render(request, 'dashboard/sub-category.html', {'form': form})


def subcategory_del(request, slug):
    post = get_object_or_404(Subcategory, slug=slug)
    post.delete()
    return redirect('subcategory_list')  # request, 'dashboard/sub-category.html', {'post': post})


def subcategory_detail(request, slug):
    post = get_object_or_404(Subcategory, slug=slug)
    return redirect('subcategory_list')  # request, 'dashboard/sub-category.html', {'post': post})


def subcategory_list(request):
    if request.method == "POST":
        form = SubcategoryForm(request.POST, request.FILES)
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.user = request.user
            subcategory.save()
            subcategoryurl = '/dashboard/product-categories/subcategory-list/'
            return redirect(subcategoryurl)
    else:
        form = SubcategoryForm()
    allsubcategory = Subcategory.objects.all()
    allmaincategory = Maincategory.objects.all()
    allsupercategory = Supercategory.objects.all()
    return render(request, 'dashboard/sub-category.html', locals())


def attributeslist(request):
    allattributesname = Attribute.objects.all()
    return render(request, 'dashboard/attributes.html', {'allattributesname': allattributesname})


def attributeslist_edit(request, slug):
    post = get_object_or_404(Attribute, slug=slug)
    if request.method == "POST":
        form = AttributeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('attributeslist')
    else:
        form = AttributeForm(instance=post)
    return render(request, 'dashboard/attributes-edit.html', {'form': form})


def add_attributes(request):
    if request.method == "POST":
        form = AttributeForm(request.POST)
        if form.is_valid():
            attribute = form.save(commit=False)
            attribute.user = request.user
            attribute.save()
            return redirect('attributeslist')
    else:
        form = AttributeForm()
    return render(request, 'dashboard/add-attributes.html', {'form': form})


def attribute_detail(request, slug):
    post = get_object_or_404(Attribute, slug=slug)
    return redirect('attributeslist')  # render(request, 'dashboard/attributes-detail.html', {'post': post})


def attribute_del(request, slug):
    post = get_object_or_404(Attribute, slug=slug)
    post.delete()
    return redirect('attributeslist')


def configureslist(request, slug):
    if request.method == "POST":
        form = ConfiguresForm(request.POST)
        if form.is_valid():
            configure = form.save(commit=False)
            configure.user = request.user
            configure.attribute = Attribute.objects.get(slug=slug)
            configure.save()
            aaaa = '/dashboard/product/attribute/configureslist/' + str(slug)
            return redirect(aaaa)
    else:
        form = ConfiguresForm()
    allconfiguresname = Configure.objects.filter(attribute__slug=slug)
    return render(request, 'dashboard/flaver-add.html', locals())


def configlist_edit(request, slug):
    post = get_object_or_404(Configure, slug=slug)
    if request.method == "POST":
        form = ConfiguresForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('attributeslist')
    else:
        form = ConfiguresForm(instance=post)
    return render(request, 'dashboard/flaver-edit.html', {'form': form})


# def del_all_config(request, pk):
#     all_config = Configure.objects.filter(attribute__id=pk)
#     dd = all_config.delete()
#     return render(request, 'dashboard/flaver-add.html', locals())

def del_all_config(request, slug):
    all_config = Configure.objects.all(attribute__slug=slug).delete()
    return render(request, 'dashboard/flaver-add.html', locals())


def config_del(request, slug):
    post = get_object_or_404(Configure, slug=slug)
    post.delete()
    return redirect('attributeslist')


def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogs = form.save(commit=False)
            blogs.user = request.user
            blogs.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    allblogcategory = Blogcategory.objects.filter()
    return render(request, 'dashboard/add-blog.html', locals())


def blog_list(request):
    blogs = Blog.objects.filter()
    allblogcategory = Blogcategory.objects.filter()
    return render(request, 'dashboard/list-blog.html', locals())
    # return render(request, 'dashboard/blog-list.html', {'blogs': blogs})


def blog_del(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    post.delete()
    return redirect('blog_list')


def bloglist_edit(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=post)
    allblogcategory = Blogcategory.objects.filter()
    # return redirect('blog_list', {'form': form})
    return render(request, 'dashboard/edit-blog.html', locals())


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return redirect('blog_list')  # return render(request, 'dashboard/blog-detail.html', {'post': post})


def blogcategory_list(request):
    blogcategorylist = Blogcategory.objects.filter()
    return render(request, 'dashboard/blog-category-list.html', locals())


def add_blogcategory(request):
    if request.method == "POST":
        form = BlogcategoryForm(request.POST, request.FILES)
        if form.is_valid():
            blogcategorys = form.save(commit=False)
            blogcategorys.user = request.user
            blogcategorys.save()
            return redirect('blogcategory_list')
    else:
        form = BlogcategoryForm()
        return render(request, 'dashboard/add-blog-category.html', locals())


def blogcategory_del(request, slug):
    post = get_object_or_404(Blogcategory, slug=slug)
    post.delete()
    return redirect('blogcategory_list')


def blogcategorylist_edit(request, slug):
    post = get_object_or_404(Blogcategory, slug=slug)
    if request.method == "POST":
        form = BlogcategoryForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('blogcategory_list')
    else:
        form = BlogcategoryForm(instance=post)
    # return redirect('blogcategory_list', {'form': form})
    return render(request, 'dashboard/edit-blog-category.html', {'form': form})


def blogcategory_detail(request, slug):
    post = get_object_or_404(Blogcategory, slug=slug)
    return redirect(
        'blogcategory_list')  # return render(request, 'dashboard/blog-category-detail.html', {'post': post})


##################################### simple login/signup & otplogin #############################


def simplelogin(request):
    if request.method == 'POST':
        loginform = SimpleLoginForm(request.POST, request.FILES)
        try:
            if loginform.is_valid():
                email = loginform.cleaned_data.get('email')
                raw_password = loginform.cleaned_data.get('password')
                user = authenticate(email=email, password=raw_password)
                login(request, user)
                return redirect('simplelogin')
        except Exception:
            messages.error(request, "Email not exist!")
    else:
        loginform = SimpleLoginForm()
    return render(request, 'index.html', {'loginform': loginform})


def simplesignup(request):
    if request.method == 'POST':
        form = SimpleSignUpForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                login(request, user)
                return redirect('simplesignup')
        except Exception:
            messages.error(request, "Email and password not recognize!")
    else:
        form = SimpleSignUpForm()
    vendors = User.objects.filter(role__role_id=3)
    return render(request, 'index.html', {'form': form, 'vendors': vendors})


def signin_with_phone(request):
    digits = [i for i in range(0, 10)]
    generated_otp = ""
    for i in range(5):
        index_1 = math.floor(random.random() * 10)
        generated_otp += str(digits[index_1])
    print(generated_otp)
    form = SignUpForm()
    if 'step1_phone' in request.POST:
        entered_phone_number = request.POST['phone_number']
        print(entered_phone_number, type(entered_phone_number))
        if User.objects.filter(phone=entered_phone_number).exists():
            user = User.objects.get(phone=entered_phone_number)
            user.otp = generated_otp
            user.set_password(generated_otp)
            user.otp_expired = False
            user.save()
            check_message_sent = sendotp(key, entered_phone_number, generated_otp)
            if check_message_sent:
                return render(request, 'confirm_otp.html', locals())
            else:
                phone_error = True
                print("error")
            print("exists")
        else:
            form = SignUpForm(request.POST)
            print(form)
            # if form.is_valid():
            user = User.objects.create_user(username=str(request.POST['phone_number']),
                                            password=generated_otp,
                                            is_active=False,
                                            # is_seller = True,
                                            otp=generated_otp,
                                            otp_expired=False,
                                            phone=str(request.POST['phone_number']))

            phone_number = request.POST['phone_number']

            check_message_sent = sendotp(key, phone_number, generated_otp)
            if check_message_sent:
                return render(request, 'confirm_otp.html', locals())
            else:
                phone_error = True

    if 'otp_entered' in request.POST:
        entered_phone_number = request.POST['entered_phone_number']
        entered_otp = request.POST['otp']
        user = User.objects.get(phone=entered_phone_number)
        if check_password(entered_otp, user.password):
            print("matched")
            if not user.otp_expired:
                user.otp_expired = False
                user.is_active = True
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # login(request, user)
                return redirect('simplesignup')
            elif user.otp_expired:
                otp_expired = True
                return render(request, 'confirm_otp.html', locals())


        else:
            otp_expired = True
            return render(request, 'confirm_otp.html', locals())
    return render(request, 'index.html', locals())


def otp_check(request):
    return render(request, 'confirm_otp.html', locals())


############################################# end otp ############################


def variant_display(request):
    variant = Variants.objects.filter()
    return render(request, 'dashboard/variant.html', {'variant': variant})


def product_list(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    allproducts = Product.objects.filter()
    return render(request, 'dashboard/product-list.html', locals())


def product_del(request, slug):
    post = get_object_or_404(Product, slug=slug)
    post.delete()
    return redirect('product_list')


def product_edit(request, slug):
    post = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            proediturl = '/dashboard/product/product-list/'
            return redirect(proediturl)
    else:
        form = ProductForm(instance=post)
    return redirect('product_list',
                    {'form': form})  # return render(request, 'dashboard/product-edit.html', {'form': form})


def product_list_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            person_change = '/person_update_view/'
            return redirect(person_change, pk=pk)
    return render(request, 'dashboard/product-list.html', {'form': form})


# AJAX
def load_configures(request):
    attribute_id = request.GET.get('attribute_id')
    configs = Configure.objects.filter(attribute_id=attribute_id).all()
    return render(request, 'dashboard/product-configure-select.html', {'configs': configs})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def product_detail_popup(request, slug):
    post = get_object_or_404(Product, slug=slug)
    return redirect('product_list', locals())  # return render(request, 'dashboard/product-list.html', {'post': post})


def product_detail(request, id, slug):
    query = request.GET.get('q')
    category = Subcategory.objects.all()
    product = Product.objects.get(pk=id)
    post = get_object_or_404(Product, id=id)
    product_image = Productgalleryimage.objects.filter(product=post)
    images = Images.objects.filter(product_id=id)
    # comments = Comment.objects.filter(product_id=id,status='True')
    context = {'product': product, 'category': category, 'images': images, 'product_image': product_image}
    if product.variant != "None":  # Product have variants
        if request.method == 'POST':  # if we select color
            variant_id = request.POST.get('variantid')
            products = Product.objects.filter()
            variant = Variants.objects.get(id=variant_id)  # selected product by click color radio
            colors = Variants.objects.filter(product_id=id, size_id=variant.size_id)
            sizes = Variants.objects.raw('SELECT * FROM  tiffenapp_variants  WHERE product_id=%s GROUP BY size_id',
                                         [id])
            query += variant.title + ' Size:' + str(variant.size) + ' Color:' + str(variant.color)
        else:
            products = Product.objects.filter()
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id, size_id=variants[0].size_id)
            sizes = Variants.objects.raw('SELECT * FROM  tiffenapp_variants  WHERE product_id=%s GROUP BY size_id',
                                         [id])
            variant = Variants.objects.get(id=variants[0].id)
        context.update({'sizes': sizes, 'colors': colors, 'variant': variant, 'query': query, 'products': products})
    return render(request, 'dashboard/product-detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        # context = {
        #     'size_id': size_id,
        #     'productid': productid,
        #     'colors': colors,
        # }
        # data = {'rendered_table': render_to_string('', context=context)}
        return render(request, 'dashboard/color_list.html', locals())
