from django.urls import path
from . import views
print('url page')
urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('passwordreset',views.Passwordreset,name="passwordreset"),
    path('newpassword',views.newpassword,name="newpassword"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),

    

]