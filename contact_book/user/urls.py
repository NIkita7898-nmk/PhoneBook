from django.contrib import admin
from django.urls import path
# from user.views import Home, Register, login_view, logout_view, p
from user import views as vs
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", vs.Home.as_view(), name="home"),
    path("register/", vs.Register.as_view(),name="register"),
    path("profile/", vs.ProfileView.as_view(),name="profile"),
    path("login/", vs.login_view, name="login"),
    path('logout/', vs.logout_view, name="logout"),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)