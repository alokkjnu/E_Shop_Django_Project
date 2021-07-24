from django.conf.urls import url
from django.urls import path, include, re_path
from . import views

app_name = 'shop'
"""
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\W]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\W]+)/$', views.product_detail, name='product_detail'),
]
"""
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug>/', views.product_detail, name='product_detail'),
]
