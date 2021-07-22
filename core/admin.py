from django.contrib import admin
from .models import *




class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'ammount', 'category_type')
    list_filter = ('name', 'date', 'ammount', 'category_type')

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category)
admin.site.register(tasks)

# Register your models here.
