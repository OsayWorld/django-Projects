from django.urls import path
from .views import portfolio_view, about_page, contact_page, dashboard, login_view, logout_view, register

urlpatterns = [
    path('', portfolio_view, name='home'),  # Set portfolio as the homepage
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
