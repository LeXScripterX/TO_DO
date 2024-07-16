from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.task_list, name='task_list'),
    path('new/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),



     path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
     path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)