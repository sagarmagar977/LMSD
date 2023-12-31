from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'books-Info', BookinfoView, basename='book')
router.register(r'returned-Books', ReturnedBookInfoView, basename='returned-book')
router.register(r'borrowed-Books', BorrowedBookInfoView, basename='borrowed-book')
router.register(r'BorrowAPI',UserBorrowview)
router.register(r'ReturnAPI',UserReturnview)
router.register(r'borrowedbooksbyuser',BorrowedBooksByUserView)
router.register(r'returnedbooksbyuser',ReturneddBooksByUserView)



urlpatterns = [
    path('book/', include(router.urls)),
    # path('book/transaction/', TransactionView.as_view(), name='transaction-view'),
    # other paths...
]
