from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('loginpage/', views.loginPage, name="loginpage"),
    path('registerpage/', views.registerPage, name="registerpage"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('', views.home, name='home'),
    path('profile/', views.profile, name="profile"),
    path("TOI", views.TOI, name='TOI'),
    path("Zeenews", views.Zeenews, name='zeenews'),
    path("cricketlivescore", views.Cricket, name='cricketlivescore'),
    path("rss", views.rss, name='RSS'),
    path("contact/", views.contact, name='contact'),
    path("live_score/", views.live_score, name='live_score'),
    path("test/", views.test, name='test'),
    path("business/", views.business, name='business'),
]