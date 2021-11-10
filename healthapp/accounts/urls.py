
from django.urls import path 
from .views import login_view, profile_view, logout_view, signup_view

app_name = 'accounts'
urlpatterns = [ 
    #accounts/login
    # {% url 'accounts:login %}
    path('login/', login_view),
    path('profile/', profile_view),
    path('logout/', logout_view),
    path('signup/', signup_view)
]