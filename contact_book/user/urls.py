from django.contrib import admin
from django.urls import path
# from user.views import Home, Register, login_view, logout_view, p
from user import views as vs
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", vs.Home.as_view(), name="home"),
    path("register/", vs.Register.as_view(),name="register"),
    path("profile/", vs.ProfileView.as_view(),name="profile"),
    path("login/", vs.login_view, name="login"),
    path('logout/', vs.logout_view, name="logout"),
]
