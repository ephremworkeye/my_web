from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/<slug:slug>', views.post_detail, name='post_detail'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('work', views.work, name='work'),
    path('privacy', views.privacy, name='privacy'),
    path('cookies', views.cookies, name='cookies'),
    path('terms', views.terms, name='terms'),
]
