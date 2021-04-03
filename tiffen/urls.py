from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from tiffen import settings
from tiffenapp import views
# from tiffenapp.forms import MyAuthenticationForm
from django.contrib.auth import views as auth_views
# from tiffenapp.forms import SimpleOTPAuthenticationForm

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('', include('django.contrib.auth.urls')),
                  path('', views.loginhere, name='loginhere'),
                  path('home/', views.home, name='home'),
                  path('dashboard/', views.dashboard, name='dashboard'),
                  path('search/', views.search, name='search'),
                  # path('search_index/', views.search_index, name='search_index'),
                  # account url
                    #INDEX
                  path('login/', views.signin_with_phone, name='signin_with_phone'),
                  path('index/', views.simplesignup, name='simplesignup'),
                  path('user_current_location_index/', views.user_current_location_index, name='user_current_location_index'),
                  # path('login/', views.simplelogin, name='simplelogin'),
                  path('otp_check/', views.otp_check, name='otp_check'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
                  # user url
                  path('dashboard/user/admin/current-user/', views.user_current_admin, name='user_current_admin'),
                  path('dashboard/user/admin/current-user-edit/<slug:slug>/', views.current_user_edit,name='current_user_edit'),
                  # admin url
                  path('user-admin-list/', views.user_admin_list, name='user_admin_list'),
                  #  employee url
                  path('dashboard/user/employee/user-employee-list/', views.user_employee_list,name='user_employee_list'),
                  path('dashboard/user/employee/user-employee-edit/<slug:slug>/', views.user_employee_edit,name='user_employee_edit'),
                  path('dashboard/user/employee/user-employee-detail/<slug:slug>/', views.user_employee_detail,name='user_employee_detail'),
                  path('dashboard/user/employee/user-employee-del/<slug:slug>/', views.user_employee_del,name='user_employee_del'),
                  #  vendor url
                  path('dashboard/user/vendor/user-vendor-list/', views.user_vendor_list, name='user_vendor_list'),
                  path('user_vendor_edit/<slug:slug>/', views.user_vendor_edit, name='user_vendor_edit'),
                  path('dashboard/user/vendor/user-vendor-del/<slug:slug>/', views.user_vendor_del,name='user_vendor_del'),
                  path('dashboard/user/vendor/user-vendor-detail/<slug:slug>/', views.user_vendor_detail,name='user_vendor_detail'),
                  path('dashboard/user/vendor/vendor_allproducts/', views.vendor_allproducts, name='vendor_allproducts'),
                    # index  vendor url
                  path('index/user/vendor/vendor-detail-index/<slug:slug>/', views.vendor_detail_index, name='vendor_detail_index'),

                  #  customer url
                  path('dashboard/user/customer/user-customer-list/', views.user_customer_list,name='user_customer_list'),
                  path('dashboard/user/customer/user-customer-edit/<slug:slug>/', views.user_customer_edit,name='user_customer_edit'),
                  path('dashboard/user/customer/user-customer-del/<slug:slug>/', views.user_customer_del,name='user_customer_del'),
                  path('dashboard/user/customer/user-customer-detail/<slug:slug>/', views.user_customer_detail,name='user_customer_detail'),
                  # Vendor url
                  path('dashboard/manage-vendor/vendor-coupon/', views.vendor_coupon, name='vendor_coupon'),
                  # main-category url
                  path('dashboard/product-categories/maincategory-list/', views.maincategory_list,name='maincategory_list'),
                  path('dashboard/product-categories/maincategorylist-edit/<slug:slug>/', views.maincategorylist_edit,name='maincategorylist_edit'),
                  path('dashboard/product-categories/maincategory-del/<slug:slug>/', views.maincategory_del,name='maincategory_del'),
                  path('dashboard/product-categories/maincategory-detail/<slug:slug>/', views.maincategory_detail,name='maincategory_detail'),
                  # super-category url
                  path('dashboard/product-categories/supercategory-list/', views.supercategory_list,name='supercategory_list'),
                  path('dashboard/product-categories/supercategorylist-edit/<slug:slug>/', views.supercategorylist_edit,name='supercategorylist_edit'),
                  path('dashboard/product-categories/supercategory-del/<slug:slug>/', views.supercategory_del,name='supercategory_del'),
                  path('dashboard/product-categories/supercategory-detail/<slug:slug>/', views.supercategory_detail,name='supercategory_detail'),
                  # sub-category url
                  path('dashboard/product-categories/subcategory-list/', views.subcategory_list,name='subcategory_list'),
                  path('dashboard/product-categories/subcategorylist-edit/<slug:slug>/', views.subcategorylist_edit,name='subcategorylist_edit'),
                  path('dashboard/product-categories/subcategory-del/<slug:slug>/', views.subcategory_del,name='subcategory_del'),
                  path('dashboard/product-categories/subcategory-detail/<slug:slug>/', views.subcategory_detail,name='subcategory_detail'),
                  # product url
                  path('dashboard/product/product-list/', views.product_list, name='product_list'),
                  path('dashboard/product/product-del/<slug:slug>/', views.product_del, name='product_del'),
                  path('dashboard/product/product-detail-popup/<slug:slug>/', views.product_detail_popup, name='product_detail_popup'),
                  path('dashboard/product/product-detail/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
                  path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
                  path('dashboard/product/product-edit/<slug:slug>/', views.product_edit, name='product_edit'),
                  path('<int:pk>/', views.product_list_update, name='product_list_update'),
                  path('ajax/load-configures/', views.load_configures, name='load_configures'),  # AJAX-Cities
                  # attribute url
                  path('dashboard/product/attributeslist/', views.attributeslist, name='attributeslist'),
                  path('dashboard/product/attribute/add-attributes/', views.add_attributes, name='add_attributes'),
                  path('dashboard/product/attribute/attributeslist-edit/<slug:slug>/', views.attributeslist_edit, name='attributeslist_edit'),
                  path('dashboard/product/attribute/attribute-detail/<slug:slug>/', views.attribute_detail, name='attribute_detail'),
                  path('dashboard/product/attribute/attribute_del/<slug:slug>/', views.attribute_del, name='attribute_del'),
                  # path('dashboard/product/attribute/attribute-detail/<slug:slug>/product_variant', views.product_variant, name='product_variant'),
                  # config url
                  path('dashboard/product/attribute/configureslist/<slug:slug>/', views.configureslist,name='configureslist'),
                  path('dashboard/product/attribute/configlist-edit/<slug:slug>/', views.configlist_edit, name='configlist_edit'),
                  path('dashboard/product/attribute/del-config/<slug:slug>/', views.del_all_config, name='del_all_config'),
                  path('dashboard/product/attribute/config_del/<slug:slug>/', views.config_del, name='config_del'),
                  # blog url
                  path('dashboard/blogs/blog-list/', views.blog_list, name='blog_list'),
                  path('dashboard/blogs/blog-add/', views.add_blog, name='add_blog'),
                  path('dashboard/blogs/blog-del/<slug:slug>/', views.blog_del, name='blog_del'),
                  path('dashboard/blogs/bloglist-edit/<slug:slug>/', views.bloglist_edit, name='bloglist_edit'),
                  path('dashboard/blogs/blog-detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
                  # blog category
                  path('dashboard/blogs/blogcategory-list/', views.blogcategory_list, name='blogcategory_list'),
                  path('dashboard/blogs/blogcategory-add/', views.add_blogcategory, name='add_blogcategory'),
                  path('dashboard/blogs/blogcategory-del/<slug:slug>/', views.blogcategory_del, name='blogcategory_del'),
                  path('dashboard/blogs/blogcategorylist-edit/<slug:slug>/', views.blogcategorylist_edit,name='blogcategorylist_edit'),
                  path('dashboard/blogs/blogcategory-detail/<slug:slug>/', views.blogcategory_detail,name='blogcategory_detail'),
                  # Extra
                  path('variant-display/', views.variant_display, name='variant_display'),
                  # path('attributeslug/', views.attributeslug, name='attributeslug')
                  # path('tiffin_location/', views.tiffin_location, name='tiffin_location'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
