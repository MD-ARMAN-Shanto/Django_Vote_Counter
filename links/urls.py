from django.conf.urls import include, url
from . import views
from django.contrib import admin
#from django.contrib.auth.views import login_required
from django.contrib.auth.views import logout_then_login



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.LinkListView.as_view(), name='home'),
    url(r'^login/$', views.login, name= "login"),
    url(r'^register/$',views.UserFormView.as_view(), name='register'),
    url(r'^logout/$', logout_then_login, name= 'logout'),
]