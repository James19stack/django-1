from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^people/',views.people,name = 'people'),
    url('^travel/',views.travel,name = 'travel'),
    url('^food/',views.travel,name = 'food'),
    url('^personal/',views.travel,name = 'personal'),
    url('^photo/',views.travel,name = 'photo'),
    url(r'^search/', views.search_results, name='search_results')
]
