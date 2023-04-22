from django.contrib import admin
from boards import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name="home"),
    path('video/',views.video),
    path('qwiz/',views.qwiz),
    path('register/',views.register),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout),
    path('',views.index),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)