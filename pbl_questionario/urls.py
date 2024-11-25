"""
URL configuration for pbl_questionario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from questionario.views import questionario_view
from users.views import user_register_view, home_view, login_view, how_it_works_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('questionario/', questionario_view, name='questionario'),
    path('cadastro/', user_register_view, name='cadastro'),
    path('home-usuario/', home_view, name='home-usuario'),
    path('login/', login_view, name='login'),
    path('como-funciona/', how_it_works_view, name='como funciona')
]
