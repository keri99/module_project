# mymarketplace/urls.py

from django.contrib import admin
from django.urls import path
from mymarketplace.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    # 다른 URL 패턴들 추가 가능
]
