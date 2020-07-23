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
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^fb$', views.fb),
    url(r'^twitter$', views.twitter),
    url(r'^linkdien$', views.linkdien),
    url(r'^insta$', views.insta)

]