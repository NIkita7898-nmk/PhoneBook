from django.contrib import admin
from django.urls import path
from user.views import Home, Register, login_view, logout_view
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("register/", Register.as_view(),name="register"),
    path("login/", login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]
