from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter
from .views import register_view, login_view, logout_view

router = DefaultRouter()
router.register(r'task',views.TodoTaskViewSet)
urlpatterns = [
    path('', views.home, name='home') ,
    path('complete/<int:id>/', views.completed, name='completed'),
    path('deleted/<int:id>/', views.deleted, name='deleted'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('notes/', views.sticky_notes, name='sticky_notes'),
    path('api/', include(router.urls)),
]



