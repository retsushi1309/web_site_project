# contact/urls.py

from django.urls import path
from . import views

app_name = 'contact' # アプリケーションの名前空間を定義

urlpatterns = [
    path('', views.ContactFormView.as_view(), name='contact_form'), # お問い合わせフォームのURL
    path('success/', views.contact_success_view, name='contact_success'), # お問い合わせ完了ページのURL
]

# config/views.py を新しく作成する必要があるため注意。
# 仮にviews.pyがない場合は、このpath('', views.index, name='home'), は後回しにしてください。