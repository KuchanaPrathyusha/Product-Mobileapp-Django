from django.conf.urls import url
from . import views
urlpatterns = [
 # mobile_list view as a class
 url(r'^$', views.ProductListView.as_view(), name='mobile_list_cls'),
 
 # Product_list view as a function
 #url(r'^$',views.Product_list,name='Product_list'),
 
 # Product_detail view as a function
 url(r'^(?P<mobile>[-\w]+)/$',
 views.Product_detail,
 name='Product_detail'
 ),
 ]