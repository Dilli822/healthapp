
from django.urls import path
from .views import create_user_info, detail_view_of_users, list_all_user


urlpatterns = [
    #crud/list
    path('list/', list_all_user),
    path('detail/<int:user_id>/', detail_view_of_users),
    path('create/', create_user_info),
]