from django.contrib import admin
from .models import MasterModel,Product ,FormField
# Register your models here.


@admin.register(MasterModel)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('id','model_name', 'creation_date', 'template_path')
    list_filter = ('model_name',)
    search_fields = ('model_name', 'template_path')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price')
    list_filter = ('name',)
    search_fields = ('name', 'price')


# Form Fields Admin
@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('label', 'field_type', 'is_required')
    list_filter = ('field_type', 'is_required')
    search_fields = ('label',)