from django.urls import path

from main.views import index, other_page, BBLoginView, profile, BBLogoutView

app_name = 'main'

urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView, name='logout'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),

    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
]
