"""info419danca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core.views import inicial, perfil, registro, estilos, cadastrar_estilo, editar_estilo, excluir_estilo, dancarinos, dancarino, editardancarino, excluirdancarino
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicial, name='inicial'),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('estilos/', estilos, name="estilos"),
    path('cadastrar/estilo', cadastrar_estilo, name="cadastrar_estilo"),
    path('editar/estilo/<int:id>', editar_estilo, name="editar_estilo"),
    path('excluir/estilo/<int:id>', excluir_estilo, name="excluir_estilo"),
    path('dancarinos/', dancarinos, name="dancarinos"),
    path('cadastrar/dancarino', dancarino, name="dancarino"),
    path('editar/dancarino/<int:id>/', editardancarino, name="editardancarino"),
    path('excluir/dancarino/<int:id>/', excluirdancarino, name="excluirdancarino"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

