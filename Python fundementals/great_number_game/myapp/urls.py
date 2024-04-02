from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('user_guess',views.check_user_number),
    path('delete_session',views.delete_session),
    path('add_winner',views.add_winner),
    path('show_winners',views.show_winners),
    path('go_back',views.back),
]
