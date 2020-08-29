from . import views
from django.urls import path

urlpatterns = [
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('update/<int:post_id>/', views.update, name='update'),
    path('regist/', views.regist, name='regist'),
]
