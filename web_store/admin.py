from django.contrib import admin
from .models import Item,Cart,CartItem,Comment
# Register your models here.

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Comment)

