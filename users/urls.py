from django.urls import path
from .views import signup, signout, signin

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    path('signin/', signin, name='signin')
]