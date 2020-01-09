from django.urls import path
from . import views


urlpatterns = [
    path('create/',views.create,name='create'),
    path('thankyou/',views.create,name='thankyou')


]
