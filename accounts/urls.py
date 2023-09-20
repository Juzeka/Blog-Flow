from django.urls import path, include
from accounts.views import (
    CreateAccountViewSet,
    AccountMeViewSet,
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('', CreateAccountViewSet.as_view(actions={'post': 'create'})),
    path('me/', AccountMeViewSet.as_view(actions={'get': 'me'})),
    path(
        'auth/',
        include([
            path('token/', TokenObtainPairView.as_view()),
            path('token/refresh/', TokenRefreshView.as_view()),
        ])
    ),
]
