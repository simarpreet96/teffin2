from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, ClearableFileInput, Textarea, ChoiceField, Select
import fileinput
from .models import User, Attribute, Configure, Maincategory, Supercategory, Subcategory, Product, \
    Blog, Blogcategory, Country, City
# from django_otp.forms import OTPAuthenticationForm


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=False,max_length=100,label='')
    email = forms.EmailField(required=False,max_length=100,label='')
    phone = forms.CharField(required=True,max_length=100,label='')
    password1 = forms.CharField(required=False,max_length=100,label='')
    password2 = forms.CharField(required=False,max_length=100,label='')
    otp=forms.CharField(max_length=30, required=False, label='')
    # role = forms.CharField(required=False,max_length=100,label='')

    class Meta:
        model=User
        fields=('username','email','phone','password1', 'password2','otp','otp_expired','role')
        widgets = {
                    'phone': forms.TextInput(attrs={'class': 'form-control'}),
                    'username': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.TextInput(attrs={'class': 'form-control'}),
                    'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'otp': forms.TextInput(attrs={'class': 'form-control'}),
                    'role': forms.HiddenInput(),
                            }


class SimpleSignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=('username','email','phone','password1', 'password2','role')
        widgets = {
                    'phone': forms.TextInput(attrs={'class': 'form-control'}),
                    'username': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.TextInput(attrs={'class': 'form-control'}),
                    'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'role': forms.HiddenInput(),
                            }


class SimpleLoginForm(forms.Form):
    email = forms.EmailField(required=True,max_length=100,label='',widget=forms.EmailInput(attrs={'class': "form-control",'placeholder':'Email'}))
    password = forms.CharField(required=True,max_length=100,label='',widget=forms.PasswordInput(attrs={'class': "form-control",'placeholder':'Password'}))

    class Meta:
        model=User
        fields=('email','password')


class UserLoginForm(forms.Form):
    email = forms.CharField(required=True, max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder':'Enter Phone Number or username or Email'}))
    password = forms.CharField(required=True, max_length=254, widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder':'Enter Password'}))


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(required=False,max_length=100,label='')
#     email = forms.EmailField(required=False,max_length=100,label='')
#     phone = forms.CharField(required=True,max_length=100,label='')
#     password1 = forms.CharField(required=False,max_length=100,label='')
#     password2 = forms.CharField(required=False,max_length=100,label='')
#
#     class Meta:
#         model=User
#         fields=('username','email','phone','password1', 'password2','otp', 'role')
#         widgets = {
#                     'phone': forms.TextInput(attrs={'class': 'form-control'}),
#                     'username': forms.TextInput(attrs={'class': 'form-control'}),
#                     'email': forms.TextInput(attrs={'class': 'form-control'}),
#                     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#                     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#                     'role': forms.HiddenInput(),
#                   }
#
#
# class SimpleLoginForm(forms.Form):
#     class Meta:
#         model=User
#         fields=('phone','password')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('image','phone','username','email','role')


class VendorForm(UserCreationForm):
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('image', 'phone', 'username', 'email', 'vendor_gstno', 'password1', 'password2', 'vendor_alternatphone','role')


class CustomerForm(UserCreationForm):
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('image', 'username', 'email', 'phone', 'password1', 'password2', 'customer_address','role')


class EmployeeForm(UserCreationForm):
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('image', 'username', 'email', 'phone', 'password1', 'password2', 'employee_expiry_date', 'employee_address', 'role',
                  'employee_user_read', 'employee_user_write', 'employee_user_create', 'employee_user_delete', 'employee_user_import', 'employee_user_export',
                  'employee_product_categories_read', 'employee_product_categories_write', 'employee_product_categories_create', 'employee_product_categories_delete', 'employee_product_categories_import', 'employee_product_categories_export',
                  'employee_product_read', 'employee_product_write', 'employee_product_create', 'employee_product_delete', 'employee_product_import', 'employee_product_export',
                  'employee_manager_vendor_read', 'employee_manager_vendor_write', 'employee_manager_vendor_create', 'employee_manager_vendor_delete', 'employee_manager_vendor_import', 'employee_manager_vendor_export',
                  'employee_customer_read', 'employee_customer_write', 'employee_customer_create', 'employee_customer_delete', 'employee_customer_import', 'employee_customer_export',
                  'employee_blog_read', 'employee_blog_write', 'employee_blog_create', 'employee_blog_delete', 'employee_blog_import', 'employee_blog_export',
                  'employee_inquiry_read', 'employee_inquiry_write', 'employee_inquiry_create', 'employee_inquiry_delete', 'employee_inquiry_import', 'employee_inquiry_export',
                  'employee_exclusive_subscription_read', 'employee_exclusive_subscription_write', 'employee_exclusive_subscription_create', 'employee_exclusive_subscription_delete', 'employee_exclusive_subscription_import', 'employee_exclusive_subscription_export',
                  'employee_notification_read', 'employee_notification_write', 'employee_notification_create', 'employee_notification_delete', 'employee_notification_import', 'employee_notification_export',
                  'employee_account_read', 'employee_account_write', 'employee_account_create', 'employee_account_delete', 'employee_account_import', 'employee_account_export',
                  'employee_website_read', 'employee_website_write', 'employee_website_create', 'employee_website_delete', 'employee_website_import', 'employee_website_export',
                  'employee_mobile_read', 'employee_mobile_write', 'employee_mobile_create', 'employee_mobile_delete', 'employee_mobile_import', 'employee_mobile_export',
                  'employee_setting_read', 'employee_setting_write', 'employee_setting_create', 'employee_setting_delete', 'employee_setting_import', 'employee_setting_export')


class SupercategoryForm(forms.ModelForm):

    class Meta:
        model = Supercategory
        fields = ('image','supercategoryname')


class MaincategoryForm(forms.ModelForm):

    class Meta:
        model = Maincategory
        fields = ('image', 'maincategoryname')


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = ('image','subcategoryname', 'supercategory', 'maincategory')


class AttributeForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = ('atributesname', 'detail_text', 'slug')


class ConfiguresForm(forms.ModelForm):

    class Meta:
        model = Configure
        fields = ('configuresname', 'detail_text')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name','price','main_image','detail_text','category', 'type', 'discount', 'attribute', 'configure')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': "form-control"}),
            'main_image':ClearableFileInput(attrs={'class': 'form-control'}),
            'detail_text': TextInput(attrs={'class': 'form-control'}),     #Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': "form-control"}),
            'type': Select(attrs={'class': 'form-control'}),
            'discount': TextInput(attrs={'class': 'form-control'}),
            'attribute': Select(attrs={'class': "form-control"}),
            'configure': Select(attrs={'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['configure'].queryset = Configure.objects.none()
    #
    #     if 'attribute' in self.data:
    #         try:
    #             attribute_id = int(self.data.get('attribute'))
    #             self.fields['configure'].queryset = Configure.objects.filter(attribute_id=attribute_id).order_by('slug')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['configure'].queryset = self.instance.attribute.configure_set.order_by('slug')


class BlogcategoryForm(forms.ModelForm):

    class Meta:
        model = Blogcategory
        fields = ('blogcategoryname', 'image', 'slug', 'description')


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'description', 'image', 'blogcategory', 'meta_title', 'meta_keyword', 'meta_description', 'slug')