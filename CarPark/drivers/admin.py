from django.contrib import admin
from .models import Driver
# Register your models here.

# class DriverAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'created_at')
#     list_display_links = ('id', 'first_name', 'last_name')
#     search_fields = ('id', 'first_name', 'last_name', 'created_at')
#     list_filter = ('id', 'first_name', 'last_name', 'created_at')


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('title',)
#     search_fields = ('title',)


admin.site.register(Driver)
# admin.site.register(Category, CategoryAdmin)s