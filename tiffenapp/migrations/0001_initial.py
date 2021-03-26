# Generated by Django 2.2.18 on 2021-03-26 07:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(upload_to='media/user/')),
                ('slug', models.SlugField(unique=True)),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('otp', models.CharField(default='', max_length=30, null=True)),
                ('otp_expired', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('vendor_gstno', models.IntegerField(blank=True, null=True, unique=True)),
                ('vendor_alternatphone', models.CharField(blank=True, max_length=10, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=30, null=True)),
                ('employee_expiry_date', models.DateTimeField(blank=True, null=True)),
                ('employee_address', models.CharField(blank=True, max_length=30, null=True)),
                ('employee_user_read', models.BooleanField(blank=True, null=True)),
                ('employee_user_write', models.BooleanField(blank=True, null=True)),
                ('employee_user_create', models.BooleanField(blank=True, null=True)),
                ('employee_user_delete', models.BooleanField(blank=True, null=True)),
                ('employee_user_import', models.BooleanField(blank=True, null=True)),
                ('employee_user_export', models.BooleanField(blank=True, null=True)),
                ('employee_product_categories_read', models.BooleanField(blank=True, null=True)),
                ('employee_product_categories_write', models.BooleanField(blank=True, null=True)),
                ('employee_product_categories_create', models.BooleanField(blank=True, null=True)),
                ('employee_product_categories_delete', models.BooleanField(blank=True, null=True)),
                ('employee_product_categories_import', models.BooleanField(blank=True, null=True)),
                ('employee_product_categories_export', models.BooleanField(blank=True, null=True)),
                ('employee_product_read', models.BooleanField(blank=True, null=True)),
                ('employee_product_write', models.BooleanField(blank=True, null=True)),
                ('employee_product_create', models.BooleanField(blank=True, null=True)),
                ('employee_product_delete', models.BooleanField(blank=True, null=True)),
                ('employee_product_import', models.BooleanField(blank=True, null=True)),
                ('employee_product_export', models.BooleanField(blank=True, null=True)),
                ('employee_manager_vendor_read', models.BooleanField(blank=True, null=True)),
                ('employee_manager_vendor_write', models.BooleanField(blank=True, null=True)),
                ('employee_manager_vendor_create', models.BooleanField(blank=True, null=True)),
                ('employee_manager_vendor_delete', models.BooleanField(blank=True, null=True)),
                ('employee_manager_vendor_import', models.BooleanField(blank=True, null=True)),
                ('employee_manager_vendor_export', models.BooleanField(blank=True, null=True)),
                ('employee_customer_read', models.BooleanField(blank=True, null=True)),
                ('employee_customer_write', models.BooleanField(blank=True, null=True)),
                ('employee_customer_create', models.BooleanField(blank=True, null=True)),
                ('employee_customer_delete', models.BooleanField(blank=True, null=True)),
                ('employee_customer_import', models.BooleanField(blank=True, null=True)),
                ('employee_customer_export', models.BooleanField(blank=True, null=True)),
                ('employee_blog_read', models.BooleanField(blank=True, null=True)),
                ('employee_blog_write', models.BooleanField(blank=True, null=True)),
                ('employee_blog_create', models.BooleanField(blank=True, null=True)),
                ('employee_blog_delete', models.BooleanField(blank=True, null=True)),
                ('employee_blog_import', models.BooleanField(blank=True, null=True)),
                ('employee_blog_export', models.BooleanField(blank=True, null=True)),
                ('employee_inquiry_read', models.BooleanField(blank=True, null=True)),
                ('employee_inquiry_write', models.BooleanField(blank=True, null=True)),
                ('employee_inquiry_create', models.BooleanField(blank=True, null=True)),
                ('employee_inquiry_delete', models.BooleanField(blank=True, null=True)),
                ('employee_inquiry_import', models.BooleanField(blank=True, null=True)),
                ('employee_inquiry_export', models.BooleanField(blank=True, null=True)),
                ('employee_exclusive_subscription_read', models.BooleanField(blank=True, null=True)),
                ('employee_exclusive_subscription_write', models.BooleanField(blank=True, null=True)),
                ('employee_exclusive_subscription_create', models.BooleanField(blank=True, null=True)),
                ('employee_exclusive_subscription_delete', models.BooleanField(blank=True, null=True)),
                ('employee_exclusive_subscription_import', models.BooleanField(blank=True, null=True)),
                ('employee_exclusive_subscription_export', models.BooleanField(blank=True, null=True)),
                ('employee_notification_read', models.BooleanField(blank=True, null=True)),
                ('employee_notification_write', models.BooleanField(blank=True, null=True)),
                ('employee_notification_create', models.BooleanField(blank=True, null=True)),
                ('employee_notification_delete', models.BooleanField(blank=True, null=True)),
                ('employee_notification_import', models.BooleanField(blank=True, null=True)),
                ('employee_notification_export', models.BooleanField(blank=True, null=True)),
                ('employee_account_read', models.BooleanField(blank=True, null=True)),
                ('employee_account_write', models.BooleanField(blank=True, null=True)),
                ('employee_account_create', models.BooleanField(blank=True, null=True)),
                ('employee_account_delete', models.BooleanField(blank=True, null=True)),
                ('employee_account_import', models.BooleanField(blank=True, null=True)),
                ('employee_account_export', models.BooleanField(blank=True, null=True)),
                ('employee_website_read', models.BooleanField(blank=True, null=True)),
                ('employee_website_write', models.BooleanField(blank=True, null=True)),
                ('employee_website_create', models.BooleanField(blank=True, null=True)),
                ('employee_website_delete', models.BooleanField(blank=True, null=True)),
                ('employee_website_import', models.BooleanField(blank=True, null=True)),
                ('employee_website_export', models.BooleanField(blank=True, null=True)),
                ('employee_mobile_read', models.BooleanField(blank=True, null=True)),
                ('employee_mobile_write', models.BooleanField(blank=True, null=True)),
                ('employee_mobile_create', models.BooleanField(blank=True, null=True)),
                ('employee_mobile_delete', models.BooleanField(blank=True, null=True)),
                ('employee_mobile_import', models.BooleanField(blank=True, null=True)),
                ('employee_mobile_export', models.BooleanField(blank=True, null=True)),
                ('employee_setting_read', models.BooleanField(blank=True, null=True)),
                ('employee_setting_write', models.BooleanField(blank=True, null=True)),
                ('employee_setting_create', models.BooleanField(blank=True, null=True)),
                ('employee_setting_delete', models.BooleanField(blank=True, null=True)),
                ('employee_setting_import', models.BooleanField(blank=True, null=True)),
                ('employee_setting_export', models.BooleanField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('atributesname', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('detail_text', models.TextField(blank=True, max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='checkboxcheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fresher', models.BooleanField(default=True)),
                ('experience', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Configure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('configuresname', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('detail_text', models.TextField(blank=True, max_length=150)),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_attributes', to='tiffenapp.Attribute')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Healthy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('maincategoryname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/category/maincategory')),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, default='', max_length=255, unique=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('main_image', models.ImageField(upload_to='media/products')),
                ('detail_text', models.TextField(blank=True, max_length=150)),
                ('type', models.CharField(choices=[('veg', 'veg'), ('non-veg', 'non-veg')], default=True, max_length=20)),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
                ('variant', models.CharField(choices=[('None', 'None'), ('size', 'size'), ('color', 'color'), ('size-color', 'size-color')], default='None', max_length=10)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiffenapp.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('employee', 'employee'), ('vendor', 'vendor'), ('customer', 'customer')], max_length=20, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image_id', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('slug', models.SlugField(unique=True)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Product')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Supercategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supercategoryname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/category/supercategory')),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategoryname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/category/subcategory')),
                ('slug', models.SlugField(unique=True)),
                ('maincategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Maincategory')),
                ('supercategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Supercategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Productvariant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('size', models.CharField(choices=[('large', 'large'), ('medium', 'medium'), ('extra-large', 'extra-large')], default=True, max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Productgalleryimage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gallery_image', models.ImageField(blank=True, upload_to='media/products/gallery/')),
                ('slug', models.SlugField(unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='tiffenapp.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiffenapp.City'),
        ),
        migrations.AddField(
            model_name='product',
            name='configure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiffenapp.Configure'),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiffenapp.Country'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField(unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Product')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffenapp.Country'),
        ),
        migrations.CreateModel(
            name='Blogcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blogcategoryname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/blogs/blogcategory/')),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(default='', upload_to='media/blogs/blog/')),
                ('meta_title', models.CharField(max_length=200)),
                ('meta_keyword', models.CharField(max_length=100)),
                ('meta_description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('blogcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiffenapp.Blogcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]