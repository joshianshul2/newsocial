#
# from django.urls import path
# from . import  views
# from django.contrib import admin
# from django.urls import path
#
#
# # from socialcustom.views import login_view , logout_view
#
# urlpatterns = [
#     path("",views.signup,name="aj"),
#     path("index", views.index, name='index.html'),
#     path("enter", views.enter, name='Enter'),
#     # path('login', views.login_view,name='login_view'),
#     path("login",views.dsa,name='login')
#     # path('logout', logout_view)
#
# ]
# # from django.contrib import admin
# # from django.urls import path
# #
# # from .views import home
# #
# # from accounts.views import login_view, register_view, logout_view
# #
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', home),
# #     path('accounts/login/', login_view),
# #     path('accounts/register/', register_view),
# #     path('accounts/logout/', logout_view)
# # ]

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^fb$', views.fb),
    url(r'^twitter$', views.twitter),
    url(r'^linkdien$', views.linkdien),
    url(r'^insta$', views.insta),
    url(r'^profile$', views.profile),
    url(r'^aboutus$', views.aboutus),
    url(r'^saveprofile1$', views.saveprofile1),
    url(r'^saveprofile2$', views.saveprofile2),
    url(r'^about_me$', views.about_me),
    url(r'^fbapi$', views.fbapi)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)