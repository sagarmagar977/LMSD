from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('groupview',GroupView)
router.register('userview',userview)

urlpatterns = [
    
    path('login/',Login),
    path('register/',register),
    path('user/',include(router.urls)),
    path('group-users/<str:group_name>/', UsersByGroupAPIView.as_view(), name='group-users'),
]
