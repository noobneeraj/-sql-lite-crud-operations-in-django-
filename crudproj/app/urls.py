from django.urls import path,include
from app import views


urlpatterns =[
    path('',views.index,name='index'),
    path('insert',views.insert,name='insert'),
    path('update/<id>',views.updateData,name='updateData'),
    path('delete/<id>',views.deleteData,name='deleteData'),
]