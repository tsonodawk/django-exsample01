# from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'crud'

urlpatterns = [
    path('members/', views.index, name='index'),
    path('members/add/', views.edit, name='add'),
    path('members/edit/<int:id>/', views.edit, name='edit'),
    path('members/delete/<int:id>/', views.delete, name='delete'),
    path('members/detail/<int:id>/', views.detail, name='detail'),
]

# url(r'^members/$', views.index, name='index'),
# url(r'^members/add/$', views.edit, name='add'),
# url(r'^members/edit/(?P<id>\d+)/$', views.edit, name='edit'),
# url(r'^members/delete/(?P<id>\d+)/$', views.delete, name='delete'),
# url(r'^members/detail/(?P<id>\d+)/$', views.detail, name='detail'),
