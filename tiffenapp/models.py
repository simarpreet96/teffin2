from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify
from django.utils.safestring import mark_safe
import math
# from django.contrib.gis.geoip2 import GeoIP2
# from phonenumber_field.modelfields import PhoneNumberField
# from django_unique_slugify import unique_slugify


class Role(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('admin', 'admin'),
        ('employee', 'employee'),
        ('vendor', 'vendor'),
        ('customer', 'customer'),
    ]
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(choices=STATUS_CHOICES, unique=True , max_length=20)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.role)
        super(Role, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


# def get_role():
#     return Role.objects.get_or_create(role_id=1)[0]


class Currentlocation(models.Model):
    # currentlocation = models.DecimalField(decimal_places=2, max_digits=4)
    currentlocation = models.CharField(max_length=250, null=True, blank=True)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(unique=True, null=False, max_length=10)
    username = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='media/user/')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False, blank=False)
    is_staff = models.BooleanField(_('staff status'), default=True)
    is_active = models.BooleanField(_('active'), default=True)
    otp = models.CharField(default="", max_length=30, null=True, blank=True)
    otp_expired = models.BooleanField(default=True)
    published_date = models.DateTimeField(blank=True, null=True)
    # vendor
    vendor_gstno = models.IntegerField(unique=True, null=True, blank=True)
    vendor_alternatphone = models.CharField(max_length=10, null=True, blank=True)
    vendor_location = models.CharField(max_length=250, null=True, blank=True)
    vendor_description = models.TextField(blank=True, null=True, max_length=150)
    vendor_longitude = models.DecimalField(decimal_places=2 , max_digits=4, blank=True, null=True)
    vendor_latitude = models.DecimalField(decimal_places=2 , max_digits=4, blank=True, null=True)
    # customer
    customer_address = models.CharField(max_length=30, blank=True, null=True)
    # employee
    employee_expiry_date = models.DateTimeField(blank=True, null=True)
    employee_address = models.CharField(max_length=30, blank=True, null=True)
                        # employee_user
    employee_user_read = models.BooleanField(blank=True, null=True)
    employee_user_write = models.BooleanField(blank=True, null=True)
    employee_user_create = models.BooleanField(blank=True, null=True)
    employee_user_delete = models.BooleanField(blank=True, null=True)
    employee_user_import = models.BooleanField(blank=True, null=True)
    employee_user_export = models.BooleanField(blank=True, null=True)
                        # employee_product_categories
    employee_product_categories_read = models.BooleanField(blank=True, null=True)
    employee_product_categories_write = models.BooleanField(blank=True, null=True)
    employee_product_categories_create = models.BooleanField(blank=True, null=True)
    employee_product_categories_delete = models.BooleanField(blank=True, null=True)
    employee_product_categories_import = models.BooleanField(blank=True, null=True)
    employee_product_categories_export = models.BooleanField(blank=True, null=True)
                        # employee_product
    employee_product_read = models.BooleanField(blank=True, null=True)
    employee_product_write = models.BooleanField(blank=True, null=True)
    employee_product_create = models.BooleanField(blank=True, null=True)
    employee_product_delete = models.BooleanField(blank=True, null=True)
    employee_product_import = models.BooleanField(blank=True, null=True)
    employee_product_export = models.BooleanField(blank=True, null=True)
                        # employee_manager
    employee_manager_vendor_read = models.BooleanField(blank=True, null=True)
    employee_manager_vendor_write = models.BooleanField(blank=True, null=True)
    employee_manager_vendor_create = models.BooleanField(blank=True, null=True)
    employee_manager_vendor_delete = models.BooleanField(blank=True, null=True)
    employee_manager_vendor_import = models.BooleanField(blank=True, null=True)
    employee_manager_vendor_export = models.BooleanField(blank=True, null=True)
                        # employee_customer
    employee_customer_read = models.BooleanField(blank=True, null=True)
    employee_customer_write = models.BooleanField(blank=True, null=True)
    employee_customer_create = models.BooleanField(blank=True, null=True)
    employee_customer_delete = models.BooleanField(blank=True, null=True)
    employee_customer_import = models.BooleanField(blank=True, null=True)
    employee_customer_export = models.BooleanField(blank=True, null=True)
                        # employee_blog
    employee_blog_read = models.BooleanField(blank=True, null=True)
    employee_blog_write = models.BooleanField(blank=True, null=True)
    employee_blog_create = models.BooleanField(blank=True, null=True)
    employee_blog_delete = models.BooleanField(blank=True, null=True)
    employee_blog_import = models.BooleanField(blank=True, null=True)
    employee_blog_export = models.BooleanField(blank=True, null=True)
                        # employee_inquiry
    employee_inquiry_read = models.BooleanField(blank=True, null=True)
    employee_inquiry_write = models.BooleanField(blank=True, null=True)
    employee_inquiry_create = models.BooleanField(blank=True, null=True)
    employee_inquiry_delete = models.BooleanField(blank=True, null=True)
    employee_inquiry_import = models.BooleanField(blank=True, null=True)
    employee_inquiry_export = models.BooleanField(blank=True, null=True)
                    # employee_exclusive
    employee_exclusive_subscription_read = models.BooleanField(blank=True, null=True)
    employee_exclusive_subscription_write = models.BooleanField(blank=True, null=True)
    employee_exclusive_subscription_create = models.BooleanField(blank=True, null=True)
    employee_exclusive_subscription_delete = models.BooleanField(blank=True, null=True)
    employee_exclusive_subscription_import = models.BooleanField(blank=True, null=True)
    employee_exclusive_subscription_export = models.BooleanField(blank=True, null=True)
                    # employee_notification
    employee_notification_read = models.BooleanField(blank=True, null=True)
    employee_notification_write = models.BooleanField(blank=True, null=True)
    employee_notification_create = models.BooleanField(blank=True, null=True)
    employee_notification_delete = models.BooleanField(blank=True, null=True)
    employee_notification_import = models.BooleanField(blank=True, null=True)
    employee_notification_export = models.BooleanField(blank=True, null=True)
                        # employee_account
    employee_account_read = models.BooleanField(blank=True, null=True)
    employee_account_write = models.BooleanField(blank=True, null=True)
    employee_account_create = models.BooleanField(blank=True, null=True)
    employee_account_delete = models.BooleanField(blank=True, null=True)
    employee_account_import = models.BooleanField(blank=True, null=True)
    employee_account_export = models.BooleanField(blank=True, null=True)
                            # employee_website
    employee_website_read = models.BooleanField(blank=True, null=True)
    employee_website_write = models.BooleanField(blank=True, null=True)
    employee_website_create = models.BooleanField(blank=True, null=True)
    employee_website_delete = models.BooleanField(blank=True, null=True)
    employee_website_import = models.BooleanField(blank=True, null=True)
    employee_website_export = models.BooleanField(blank=True, null=True)
                            # employee_mobile
    employee_mobile_read = models.BooleanField(blank=True, null=True)
    employee_mobile_write = models.BooleanField(blank=True, null=True)
    employee_mobile_create = models.BooleanField(blank=True, null=True)
    employee_mobile_delete = models.BooleanField(blank=True, null=True)
    employee_mobile_import = models.BooleanField(blank=True, null=True)
    employee_mobile_export = models.BooleanField(blank=True, null=True)
                        # employee_setting
    employee_setting_read = models.BooleanField(blank=True, null=True)
    employee_setting_write = models.BooleanField(blank=True, null=True)
    employee_setting_create = models.BooleanField(blank=True, null=True)
    employee_setting_delete = models.BooleanField(blank=True, null=True)
    employee_setting_import = models.BooleanField(blank=True, null=True)
    employee_setting_export = models.BooleanField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'username']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


# class Profile(models.Model):
#     objects = None
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=10)
#     otp = models.CharField(max_length=6)
#
#     def __str__(self):
#         return self.phone


class Supercategory(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supercategoryname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/category/supercategory')
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.supercategoryname)
        super(Supercategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.supercategoryname


class Maincategory(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maincategoryname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/category/maincategory')
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.maincategoryname)
        super(Maincategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.maincategoryname


class Subcategory(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategoryname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/category/subcategory')
    supercategory = models.ForeignKey(Supercategory, on_delete=models.CASCADE, null=True, blank=True)
    maincategory = models.ForeignKey(Maincategory, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subcategoryname)
        super(Subcategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.subcategoryname


class Country(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, max_length=150)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, max_length=150)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('weight', 'weight'),
        ('healthy', 'healthy'),
        ('size', 'size'),
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # atributesname = models.CharField(choices=STATUS_CHOICES, default=True,unique=True, max_length=20)
    atributesname = models.CharField(unique=True, max_length=20)
    slug = models.SlugField(unique=True, null=False, blank=False)
    detail_text = models.TextField(blank=True, max_length=150)
    # configure = models.ForeignKey(Configure, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.atributesname)
        super(Attribute, self).save(*args, **kwargs)

    def __str__(self):
        return self.atributesname


class Configure(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    configuresname = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=False, blank=False)
    detail_text = models.TextField(blank=True, max_length=150)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True, blank=True, related_name="product_attributes")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.configuresname)
        super(Configure, self).save(*args, **kwargs)

    def __str__(self):
        return self.configuresname


class Product(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('veg', 'veg'),
        ('non-veg', 'non-veg'),
    ]
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    VARIANTS = (
        ('None', 'None'),
        ('size', 'size'),
        ('color', 'color'),
        # ('weight', 'weight'),
        # ('healthy', 'healthy'),
        ('size-color', 'size-color'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=255, db_index=True, default='')
    price = models.IntegerField(blank=True, null=True)
    main_image = models.ImageField(upload_to='media/products')
    detail_text = models.TextField(blank=True, max_length=150)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL,  null=True, blank=True)
    configure = models.ForeignKey(Configure, on_delete=models.SET_NULL,  null=True, blank=True)
    type = models.CharField(choices=STATUS_CHOICES, max_length=20, default=True)
    discount = models.IntegerField(null=True, blank=True, default=0)
    # location = models.PointField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    published=models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=False, blank=False)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    status=models.CharField(max_length=10,choices=STATUS)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def discount_price(self):
        p = self.price
        d = self.discount
        if d <= 0:
            return 0;
        else:
            discount_given = p * d/100
            sale_price = p-discount_given
        return sale_price


class Productgalleryimage(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    gallery_image = models.ImageField(upload_to='media/products/gallery/', blank=True)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.slug


class Images(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.title


class Color(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Variants(models.Model):
    objects = None
    title = models.CharField(max_length=100, blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True,null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True,null=True)
    # weight = models.ForeignKey(Weight, on_delete=models.CASCADE,blank=True,null=True)
    # healthy = models.ForeignKey(Healthy, on_delete=models.CASCADE,blank=True,null=True)
    image_id = models.IntegerField(blank=True,null=True,default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.title

    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""


class Productvariant(models.Model):
    STATUS_CHOICES = [
        ('large', 'large'),
        ('medium', 'medium'),
        ('extra-large', 'extra-large')
    ]
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    size = models.CharField(choices=STATUS_CHOICES, max_length=20, default=True)
    # attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    # configure = models.ForeignKey(Configure, on_delete=models.CASCADE)
    # variant = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.slug


class Weight(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Healthy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Blogcategory(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogcategoryname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/blogs/blogcategory/')
    description = models.TextField()
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.blogcategoryname)
        super(Blogcategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.blogcategoryname


class Blog(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='media/blogs/blog/',default='')
    blogcategory = models.ForeignKey(Blogcategory, on_delete=models.SET_NULL, blank=True, null=True)
    meta_title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=100)
    meta_description = models.TextField()
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class checkboxcheck(models.Model):
    fresher = models.BooleanField(default=True)
    experience = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.slug