from django.urls import path, include
from accounts.views import (
    CreateAccountViewSet,
    TokenObtainPairView,
    TokenRefreshView
)


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
