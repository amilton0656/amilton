from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('pagina1/', views.pagina1_view, name='pagina1'),
    path('pagina2/', views.pagina2_view, name='pagina2'),

    # URL para logout. 'next_page' diz para onde ir após sair.
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
