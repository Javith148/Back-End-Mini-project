from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("upload",views.upload ,name='post_create'),
    path("",views.home ,name='show'),
    path("viewall/<int:id>",views.viewDetail, name= "viewall"),
    path( "otp/",views.emailotp,name="otp"),
   
] 


