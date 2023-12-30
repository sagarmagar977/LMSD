from .models import *
from .serializers import *
from rest_framework import viewsets,mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.permission import CustomModelPermission
from rest_framework.response import Response

class BookinfoView(viewsets.ModelViewSet):
    queryset=BookInfo.objects.all()
    serializer_class=BookInfoSerializers
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    permission_classes=[CustomModelPermission]
    filterset_fields=['title','author',]
    search_fields=['title','author','catagory']

class ReturnedBookInfoView(viewsets.ModelViewSet):
    queryset=ReturnedBookInfo.objects.all()
    serializer_class=ReturnedBookInfoSerializers
    permission_classes=[CustomModelPermission]
    filterset_fields=['book','returner_name',]
    search_fields=['book','returner_name']

class BorrowedBookInfoView(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset=BorrowedBookInfo.objects.all()
    serializer_class=BorrowedBookInfoSerializers
    permission_classes=[CustomModelPermission]
    filterset_fields=['book','borrower_name',]
    search_fields=['book','borrower_name']

class UserBorrowview(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset=Transaction.objects.all()
    serializer_class=UserTransactionBorrowSerializers
    permission_classes=[CustomModelPermission]

    def perform_create(self, serializer):
        serializer.validated_data['transaction_type'] = "Borrow"
        serializer.validated_data['transaction_date'] = timezone.now().date()
        serializer.validated_data['due_date'] = serializer.validated_data['transaction_date'] + timedelta(days=14)
        serializer.validated_data['user'] = self.request.user
        serializer.save()
        return Response("Book borrowed Succesfully !")
    

class UserReturnview(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset=Transaction.objects.all()
    serializer_class=UserTransactionReturnSerializers
    permission_classes=[CustomModelPermission]

    def perform_create(self, serializer):
        serializer.validated_data['transaction_type'] = "Return"
        serializer.validated_data['transaction_date'] = timezone.now().date()
        serializer.validated_data['user'] = self.request.user
        serializer.save()
       
        # try:
        #     serializer.save()
        #     return True, {"detail": "Book returned successfully!"}
        # except Exception as e:
        #     return False, {"detail": f"Failed to return the book. Error: {str(e)}"}
   

    