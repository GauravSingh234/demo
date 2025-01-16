from django.contrib import admin
from .models import Slider, Card, Button, Image,Video,FormField
                     
# Register your models here.

# Slider/Carousel Admin
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'order', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


# Cards Admin
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('title', 'content')


# Buttons Admin
@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('label', 'is_primary', 'action')
    list_filter = ('is_primary',)
    search_fields = ('label',)


# Images Admin
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)



# Videos Admin
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')
    search_fields = ('title',)


# Form Fields Admin
@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('label', 'field_type', 'is_required')
    list_filter = ('field_type', 'is_required')
    search_fields = ('label',)