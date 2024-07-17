from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, SignupView, LoginView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/task/new/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
