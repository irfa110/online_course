from django.urls import path 
from . views import *
from django.conf import settings
from django.conf.urls.static import static
from . auth import *

urlpatterns = [
    path("", home,name='home'),
    path('signup', signup , name='signup'),
    path('course/<str:slug>',coursepage,name='coursepage'),
    path("login",login_user,name="login"),
    path('logout',logout_view,name="logout"),
    path('checkout/<str:slug>',checkout,name='checkout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)