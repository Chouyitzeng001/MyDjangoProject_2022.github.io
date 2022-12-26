from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'tel')  # 顯示欄位


admin.site.register(Customer, CustomerAdmin)  # 加入至Administration(管理員後台)