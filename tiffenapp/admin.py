from django.contrib import admin
# import admin_thumbnails
from django.utils.html import format_html
from .models import User, Role, Product, Productgalleryimage, Productvariant, Maincategory, Supercategory, Subcategory,\
    Attribute, Configure, Blog, Blogcategory, Country, City, Images, Color, Size, Variants, Weight, Healthy, checkboxcheck
# from django.urls import reverse


class UserAdmin(admin.ModelAdmin):

    def image_post(self, obj):
        return format_html('<img src="/media/{}" width="100" height="100"/>'.format(obj.image))

    image_post.short_description = 'Image'
    list_display = ['id', 'email', 'phone', 'username', 'image_post']


admin.site.register(User, UserAdmin)
admin.site.register(Role)
# admin.site.register(Profile)

# @admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True


class ProductgalleryimageInline(admin.TabularInline):
    model = Productgalleryimage
    readonly_fields = ('id',)
    extra = 1
    show_change_link = True

class ProductAdmin(admin.ModelAdmin):
    list_display =  ['id', 'name', 'user', 'price', 'category', 'type', 'attribute', 'configure', 'slug' ]
    list_filter = ['category']
    # readonly_fields = ('image_tag',)
    inlines = [ProductImageInline,ProductVariantsInline,ProductgalleryimageInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


# admin.site.register(Role)
admin.site.register(Productgalleryimage)
admin.site.register(Productvariant)
admin.site.register(Maincategory)
admin.site.register(Supercategory)
admin.site.register(Subcategory)
admin.site.register(Blog)
admin.site.register(Blogcategory)
admin.site.register(Attribute)
admin.site.register(Configure)
admin.site.register(Country)
admin.site.register((City))

admin.site.register(Images)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variants)
admin.site.register(Weight)
admin.site.register(Healthy)

admin.site.register(checkboxcheck)


