from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("log_out/", views.log_out, name="log_out"),
    path("user_cart/", views.user_cart, name="user_cart"),

]
