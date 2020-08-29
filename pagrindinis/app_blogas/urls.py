from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blogas'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blogai'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('myblog/', views.BlogsByUserListView.as_view(), name='my_blog'),
    path('myblog/new', views.BlogsByUserCreateView.as_view(), name='my_blog_new'),

]