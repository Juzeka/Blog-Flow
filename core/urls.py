from django.contrib import admin
from django.urls import path, include


prefix_v1 = 'api/v1'

urlpatterns = [
    path(f'{prefix_v1}/accounts/', include('accounts.urls')),
    path(f'{prefix_v1}/categories/', include('categories.urls')),
    path('', admin.site.urls)
]
