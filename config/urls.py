"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include # includeをインポート
from . import views # viewsモジュールをインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'), # トップページのURLを追加
    path('worry/', views.worry, name='worry'),
    path('flow/', views.flow, name='flow'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', include('contact.urls')), # contactアプリのURLパターンを組み込む
]
