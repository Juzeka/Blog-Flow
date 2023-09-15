from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from accounts.views import CreateAccountViewSet


urlpatterns = [
    path('', CreateAccountViewSet.as_view(actions={'post': 'create'})),
    path(
        'auth/',
        include([
            path('token/', TokenObtainPairView.as_view()),
            path('token/refresh/', TokenRefreshView.as_view()),
        ])
    ),
]
