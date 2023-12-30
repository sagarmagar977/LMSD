from django.contrib import admin
from .models import *
admin.site.register(BookInfo)

admin.site.register(ReturnedBookInfo)
admin.site.register(Transaction)
admin.site.register(BorrowedBookInfo)
