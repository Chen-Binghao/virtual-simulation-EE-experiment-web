from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'add_user$', views.add_user, ), url(r'bound_jaccount$', views.bound_jaccount, ),
               url(r'user_login$', views.user_login, ), url(r'show_experiment$', views.show_experiment, ),
               url(r'show_user$', views.show_user, ),url(r'jaccount_login$', views.jaccount_login, ),
               url(r'edit_loginid$', views.edit_loginid, ),url(r'edit_password$', views.edit_password, ),
               url(r'car_score$', views.car_score, ),url(r'ex_score$', views.ex_score, ),]
