from rest_framework import serializers
from .models import *

class BookInfoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = BookInfo
        fields = "__all__"

class BorrowedBookInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBookInfo
        fields = "__all__"

class ReturnedBookInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReturnedBookInfo
        fields = "__all__"



class UserTransactionBorrowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["book"]
class UserTransactionReturnSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["book","due_date"]










